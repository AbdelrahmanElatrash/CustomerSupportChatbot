import boto3
import sys
import uuid


REGION = "us-east-1"

# Replace this with the ARN of your current Harness
HARNESS_ARN = "arn:aws:bedrock-agentcore:us-east-1:479456215827:harness/support_agent_harness-iLaD3R3mS8"

client = boto3.client("bedrock-agentcore", region_name=REGION)

# Same session ID must be reused for all turns.
session_id = str(uuid.uuid4())


def invoke(message):
    print(f"\nUser: {message}")

    response = client.invoke_harness(
        harnessArn=HARNESS_ARN,
        runtimeSessionId=session_id,
        runtimeUserId="bug-report-test-user",
        messages=[
            {
                "role": "user",
                "content": [{"text": message}],
            }
        ],
    )

    text_parts = []

    for event in response["stream"]:
        if "contentBlockDelta" in event:
            delta = event["contentBlockDelta"].get("delta", {})

            if "text" in delta:
                text = delta["text"]
                text_parts.append(text)

                print(text, end="", flush=True)

            if "toolUse" in delta:
                print("\n[tool call]")
                print(delta["toolUse"])

        elif "runtimeClientError" in event:
            print(
                f"\n[ERROR] {event['runtimeClientError']['message']}",
                file=sys.stderr,
            )

    print()
    return "".join(text_parts)


invoke("My application crashes whenever I upload a PDF.")

invoke(
    "Open Documents, click Upload, select a PDF file, "
    "and the application crashes immediately."
)

invoke(
    "Windows 11, Chrome 151, application version 2.4.1."
)