# Module 1 — Building the Agent

## Overview

Built the initial **Travel Agent** using the **Strands Agents SDK**, Amazon Bedrock, and AWS Lambda.

The agent uses a custom `flight_search` tool to provide airline options for a destination.

## What I Built

* Created a Travel Agent using Strands Agents SDK
* Integrated Amazon Bedrock with **Amazon Nova Lite**
* Created a custom `flight_search` tool
* Deployed the agent to AWS Lambda
* Tested the agent using Lambda Test Events

## Architecture Diagram

![Architecture](screenshots/Agentic_AI_Architecture.png)


## Example

**Input**

```json
{
  "prompt": "What airlines can I take to Atlanta?"
}
```

**Output**

```text
The available flight options to Atlanta are:

1. Delta Airlines
2. Southwest Airlines
```

## Troubleshooting

Initially encountered:

```text
ValidationException:
The provided model identifier is invalid.
```

Verified the available Bedrock models using AWS CLI and corrected the model identifier to:

```text
amazon.nova-lite-v1:0
```

After redeployment, the agent executed successfully.

## Key Learnings

* Created an AI Agent using Strands Agents SDK
* Created and registered a custom tool
* Integrated Strands Agents with Amazon Bedrock
* Deployed the agent using AWS Lambda
* Tested the agent using Lambda Test Events
* Troubleshot Bedrock model configuration
