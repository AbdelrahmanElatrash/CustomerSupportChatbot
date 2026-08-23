# Evaluation Evidence

## Project
Support Classification Flow with AgentCore Harness integration.

## Flow
- Flow ID: `55ET5J4N6G`
- Flow Alias ID: `SJSN755WJ0`
- Region: `us-east-1`

## Routes evaluated
- `support`
- `question`
- `other`



I remove the account id 
## Evaluation job
- Job ARN: `arn:aws:bedrock:us-east-1:[account id]:evaluation-job/8ijxs56ss95n`
- Dataset S3 URI: `s3://udacity-agentic-engineer-c1-eval-[account id]/output_eval_dataset.jsonl`
- Results prefix: `s3://udacity-agentic-engineer-c1-eval-[account id]/results/`



## Observations
- The `support` route invokes the AgentCore Harness, which uses the Gateway tool `create_bug_report` and persists support records through Lambda/DynamoDB.
- The `question` route retrieves FAQ content from the Knowledge Base and uses Amazon Nova 2 Lite to formulate the answer from retrieved results.
- The `other` route uses a fallback response that directs the user to human support and displays the configured test phone number `+971 800 123 4567`.
- The Evaluation job was created as a BYOI evaluation because the application responses were precomputed into a JSONL file.

## Evaluation Observation

The Bedrock Evaluation achieved an overall correctness score of 94.4% (8.5/9) across the nine test cases.

The results indicate that the chatbot generally produces responses that align with the expected behavior across the support, question, and other routes. Eight test cases received a full correctness score of 1.0.

The main weak case was the first support scenario, which received a score of 0.5. In that case, the chatbot asked for additional troubleshooting information instead of confirming that the support ticket had been created and providing the ticket information as expected by the reference response.

A possible next step is to refine the support-route instructions so that, when all required bug-report information is already available, the assistant creates the support record immediately instead of requesting unnecessary additional details. Additional edge cases could also be added to the evaluation dataset to test incomplete and ambiguous bug reports.

## Notes
The phone number above is a synthetic test value used for this project and is not a real support number.

this text editable by AI to fix spelling and formated as MD file 
`flow-test-template.json` generated question by AI depend on FAQ md file 
