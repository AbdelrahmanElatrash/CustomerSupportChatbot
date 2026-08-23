import json
import os
import uuid
from datetime import datetime, timezone

import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    print("EVENT:", json.dumps(event, indent=2, default=str))
    print("CONTEXT:", json.dumps(context_to_dict(context), indent=2, default=str))

    # AgentCore Gateway passes tool inputs directly in the event.
    description = str(event.get("description") or "").strip()
    steps = str(event.get("stepsToReproduce") or "").strip()
    environment = str(event.get("environment") or "").strip()

    # AgentCore metadata is available through Lambda client context.
    metadata = get_agentcore_metadata(context)

    if not description:
        return {
            "success": False,
            "error": "Missing required field: description",
            "tool": metadata.get("tool_name"),
            "requestId": metadata.get("request_id"),
        }

    ticket_id = str(uuid.uuid4())

    item = {
        "ticketId": ticket_id,
        "description": description,
        "stepsToReproduce": steps,
        "environment": environment,
        "status": "OPEN",
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }

    table.put_item(Item=item)

    return {
        "success": True,
        "ticketId": ticket_id,
        "status": "OPEN",
        "message": "Support record created successfully.",
        "requestId": metadata.get("request_id"),
    }


def get_agentcore_metadata(context):
    """
    AgentCore Gateway provides metadata through Lambda client context.
    """
    result = {}

    try:
        custom = context.client_context.custom or {}

        result["message_version"] = custom.get(
            "bedrockAgentCoreMessageVersion"
        )
        result["request_id"] = custom.get(
            "bedrockAgentCoreAwsRequestId"
        )
        result["mcp_message_id"] = custom.get(
            "bedrockAgentCoreMcpMessageId"
        )
        result["gateway_id"] = custom.get(
            "bedrockAgentCoreGatewayId"
        )
        result["target_id"] = custom.get(
            "bedrockAgentCoreTargetId"
        )
        result["tool_name"] = custom.get(
            "bedrockAgentCoreToolName"
        )

    except Exception as exc:
        print("Could not read AgentCore metadata:", str(exc))

    return result


def context_to_dict(context):
    """
    Helper used only for logging/debugging.
    """
    result = {
        "function_name": getattr(context, "function_name", None),
        "function_version": getattr(context, "function_version", None),
        "invoked_function_arn": getattr(context, "invoked_function_arn", None),
        "memory_limit_in_mb": getattr(context, "memory_limit_in_mb", None),
        "aws_request_id": getattr(context, "aws_request_id", None),
    }

    try:
        result["client_context"] = {
            "custom": context.client_context.custom
            if context.client_context
            else None
        }
    except Exception:
        result["client_context"] = None

    return result

