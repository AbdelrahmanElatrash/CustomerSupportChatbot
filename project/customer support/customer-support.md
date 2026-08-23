# AWS Agentic Support Project

## Lambda and DynamoDB

Run AWS CLI to set up Lambda and DynamoDB using `template.yaml`.

## AgentCore Harness

Create AgentCore Harness.

Create a Gateway to connect the AgentCore Harness with the Lambda function.

Add the tool to the AgentCore Harness.

### Test Agent

![Test Agent](./images/excute%20agent%20flow.png)

### Test Result

![Test Result](./images/test%20agent%202.png)

### DynamoDB Record

![DynamoDB Record](./images/data%20record.png)

---

## Knowledge Base

Create a Knowledge Base.

Create an S3 bucket and upload the FAQ file to:

`bedrock-agentic-support-kb-44as231`

Create the Knowledge Base managed vector store and synchronize the data.

![Knowledge Base](./images/knBase.png)

---

## Bedrock Flow

Create the Flow.

### Classifier Prompt Node

Create the classifier Prompt node.

Add the prompt and select Amazon Nova 2 Lite.

![Classifier](./images/classifier%20prompt%20nod%20configuer.png)

![Classifier Configuration](./images/config%20classifier%20prompt%20node.png)

### Condition Node

Create the Condition node.

![Condition](./images/condition.png)

### Support Route

Create a Lambda function to invoke the AgentCore Harness from the Flow.

Add and configure the Lambda node.

Connect the Lambda node to the Output node and test the agent ticket-creation flow.

### Question Route

Add and configure the Knowledge Base node.

![Knowledge Base Configuration](./images/KnBase%20cofig.png)

Add the FAQ Prompt node.

Use Amazon Nova 2 Lite and connect the node to the Knowledge Base.

Add the Output node and test the question flow.

### Covered Question

![cover question](./images/test_coverd_question.png)

### Uncovered Question

![Uncovered Question](./images/test%20uncoverd%20question%20\(2\).png)

### Other Route

Create the `other` Prompt node.

![Other Node](./images/other%20config.png)

Configure the `other` response.

![Other Response](./images/other%20config.png)

---

## Full Flow

![Full Flow](./images/full%20flow%20diagram.png)

---

## Evaluation

Run the evaluation process.

![Evaluation](./images/evaluation.png)

### Evaluation Score

![Score](./images/metric_score.png)


## note 
this file edit by AI to be a formated as md file
create lambda bridge function with AI
