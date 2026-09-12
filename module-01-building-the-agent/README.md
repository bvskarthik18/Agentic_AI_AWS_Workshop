# Module 1 — Building the First Travel Agent

## Overview

This module focuses on building the first version of a GenAI Travel Agent using the **Strands Agents SDK**.

The Travel Agent is deployed as an **AWS Lambda function** and uses **Amazon Bedrock with Amazon Nova Lite** as the foundation model.

The agent is equipped with a custom `flight_search` tool that provides available airline options for supported destinations.

---

## What I Built

In this module, I created a basic Travel Agent that:

* Uses the **Strands Agents SDK**
* Runs as an **AWS Lambda function**
* Uses **Amazon Bedrock**
* Uses **Amazon Nova Lite** as the foundation model
* Defines a custom `flight_search` tool
* Allows the agent to decide when to use the tool
* Returns available flight carrier options based on the user's request

---

## Architecture

```text
                         User Prompt
                              |
                              v
                       AWS Lambda
                              |
                              v
                    Strands Agents SDK
                              |
                              v
                     Amazon Nova Lite
                              |
                              v
                  Agent decides to use tool
                              |
                              v
                       flight_search()
                              |
                              v
                     Flight Options
                              |
                              v
                       Agent Response
```

---

## Project Structure

```text
module-01-building-the-agent/
│
├── README.md
├── index.py
└── screenshots/
    ├── lambda-function.png
    ├── test-event.png
    └── successful-response.png
```

---

## Implementation

The Travel Agent was implemented using Python and the Strands Agents SDK.

### `index.py`

Deployed index.py with required details provided in Agent()

---

# Testing the Agent

After deploying the Lambda function, I created a new Lambda Test Event named:

```text
Test
```

The test event contained the following JSON input:

```json
{
  "prompt": "What are the flight options to Atlanta?"
}
```

The Strands Agent processed the request and used the `flight_search` tool to retrieve the available airlines.

### Successful Response

```text
The available flight options to Atlanta are:

1. Delta Airlines
2. Southwest Airlines
```

---

# Troubleshooting

## Issue: Invalid Model Identifier

During the initial test, the Lambda function returned the following error:

```text
ValidationException:
The provided model identifier is invalid.
```

The initial model identifier used in the code was:

```text
us.amazon.nova.lite-v1:0
```

To troubleshoot the issue, I checked the available Amazon Bedrock foundation models in the `us-west-2` region using the AWS CLI.

```bash
aws bedrock list-foundation-models --region us-west-2 | grep nova
```

The command returned the following relevant model:

```text
amazon.nova-lite-v1:0
```

I updated the Agent configuration from:

```python
model="us.amazon.nova.lite-v1:0"
```

to:

```python
model="amazon.nova-lite-v1:0"
```

After updating the model identifier and redeploying the Lambda function, the test executed successfully.

### Key Lesson

The model identifier must match the model available and accessible in the AWS region being used.

Using the AWS CLI to verify available foundation models is a useful troubleshooting step when working with Amazon Bedrock.

---

# Key Concepts Learned

## 1. Strands Agents SDK

Learned how to create an AI agent using the Strands Agents SDK.

```python
travel_agent = Agent(
    model="amazon.nova-lite-v1:0",
    system_prompt=TRAVEL_AGENT_PROMPT,
    tools=[flight_search]
)
```

---

## 2. System Prompt

A system prompt was used to define the role and behavior of the Travel Agent.

The agent was instructed to act as a travel assistant and use the available tool when required.

---

## 3. Creating Tools

Created a custom tool using the Strands `@tool` decorator:

```python
@tool
def flight_search(city: str) -> dict:
```

The tool provides flight carrier information for supported destinations.

---

## 4. Agent Tool Usage

The agent can determine when it needs additional information and invoke the appropriate tool.

For example:

```text
User
  |
  | "What airlines can I take to Atlanta?"
  v
Travel Agent
  |
  | Calls flight_search("Atlanta")
  v
flight_search Tool
  |
  v
Delta Airlines
Southwest Airlines
  |
  v
Travel Agent Response
```

---

## 5. Amazon Bedrock

Amazon Bedrock was used to access the Amazon Nova Lite foundation model.

Model used:

```text
amazon.nova-lite-v1:0
```

Region:

```text
us-west-2
```

---

## 6. AWS Lambda

The Travel Agent was deployed as a serverless AWS Lambda function.

The Lambda function receives the user's prompt through the event:

```python
event.get('prompt')
```

and passes it to the Strands Agent.

---

## 7. AWS CLI Troubleshooting

The AWS CLI was used to identify the available Amazon Bedrock models:

```bash
aws bedrock list-foundation-models --region us-west-2 | grep nova
```

This helped identify the correct model ID and resolve the `ValidationException`.

---

# Module 1 Flow

The complete flow implemented in this module:

```text
1. User provides a travel request
          |
          v
2. AWS Lambda receives the request
          |
          v
3. Strands Agent processes the request
          |
          v
4. Amazon Nova Lite reasons about the request
          |
          v
5. Agent decides whether to use flight_search
          |
          v
6. flight_search returns available airlines
          |
          v
7. Agent generates the final response
```

---

# Module 1 Outcome

Successfully built and tested the first version of a Travel Agent using:

* Python
* AWS Lambda
* Amazon Bedrock
* Amazon Nova Lite
* Strands Agents SDK
* Custom Agent Tools

The agent can receive a travel-related prompt, invoke the `flight_search` tool, and return available flight carrier options.

---

# What I Learned

Through this module, I learned:

* How to create a basic AI Agent using the Strands Agents SDK
* How to define a system prompt for an agent
* How to create custom tools using `@tool`
* How an agent can decide to invoke a tool
* How to deploy an agent using AWS Lambda
* How to use Amazon Nova Lite through Amazon Bedrock
* How to troubleshoot Bedrock model identifier issues
* How to use AWS CLI to verify available foundation models
* How an AI agent connects the model, tools, and application logic

---

# Next Module

## Module 2 — Interacting with External APIs

The next module will extend the Travel Agent by integrating **external APIs**.

The goal is to move beyond static/local flight data and enable the agent to interact with external services and retrieve dynamic information.

---

## Workshop Progress

| Module   | Topic                          | Status      |
| -------- | ------------------------------ | ----------- |
| Module 1 | Building the Agent             | ✅ Completed |
| Module 2 | Interacting with External APIs | ⏳ Upcoming  |
| Module 3 | TBD                            | ⏳ Upcoming  |
| Module 4 | TBD                            | ⏳ Upcoming  |
| Module 5 | TBD                            | ⏳ Upcoming  |
| Module 6 | TBD                            | ⏳ Upcoming  |
| Module 7 | TBD                            | ⏳ Upcoming  |

---

## Technologies

* **AWS Lambda**
* **Amazon Bedrock**
* **Amazon Nova Lite**
* **Strands Agents SDK**
* **Python**
* **AWS CLI**
