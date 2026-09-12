# Building GenAI Applications with AI Agents

Hands-on implementation of the AWS workshop **[Building and Scaling Agentic AI Workflows](https://catalog.workshops.aws/workshops/eb18d538-bf1f-49b9-9747-c474953deee1/en-US)**.

This repository documents my learning, implementation, and hands-on work throughout the workshop.

## About the Workshop

The workshop focuses on building and progressively enhancing an **AI Agent** using the **Strands Agents SDK** and **Amazon Bedrock**.

Starting with a basic Travel Agent, the workshop gradually introduces tools, external APIs, memory, RAG, MCP, API integration, and observability.

## What We Build

The Travel Agent is progressively enhanced throughout the workshop:

```text
Build the Agent
      ↓
Integrate External APIs
      ↓
Add Agent Memory
      ↓
Add RAG with Knowledge Bases
      ↓
Use MCP
      ↓
Expose Agent through API Gateway
      ↓
Add Observability
      ↓
Final Agent
```

## Workshop Modules

| Module | Topic                                 | Status      |
| ------ | ------------------------------------- | ----------- |
| 1      | [Building the Agent](module-01-building-the-agent/README.md)                    | ✅ Completed |
| 2      | [Integration with External APIs](module-02-interacting-with-external-apis/README.md)        | ✅ Completed |
| 3      | Adding Agent Memory                   | 🔜 Next     |
| 4      | Using Bedrock Knowledge Bases for RAG | ⏳           |
| 5      | Using MCP                             | ⏳           |
| 6      | Exposing the Agent via API Gateway    | ⏳           |
| 7      | Adding Observability *(Optional)*     | ⏳           |
| 8      | Summary                               | ⏳           |

## Technologies

* AWS Lambda
* Amazon Bedrock
* Amazon Nova
* Strands Agents SDK
* Python
* Amazon Bedrock Knowledge Bases
* MCP
* Amazon API Gateway

## Repository Structure

```text
building-genai-ai-agents/
│
├── README.md
│
├── module-01-building-the-agent/
│   ├── README.md
│   └── index.py
│
├── module-02-integration-with-external-apis/
│   ├── README.md
│   └── index.py
│
├── module-03-agent-memory/
│   ├── README.md
│   └── ...
│
├── module-04-bedrock-knowledge-bases-rag/
│   ├── README.md
│   └── ...
│
├── module-05-mcp/
│   ├── README.md
│   └── ...
│
├── module-06-api-gateway/
│   ├── README.md
│   └── ...
│
├── module-07-observability/
│   ├── README.md
│   └── ...
│
└── module-08-summary/
    └── README.md
```

Each module contains:

* `README.md` — Module overview, implementation, testing, and key learnings
* Source code and configuration used during the module

## Goal

Build practical experience with AI Agents and understand how agents can:

* Use tools
* Interact with external APIs
* Maintain memory
* Retrieve information using RAG
* Use MCP
* Expose agent functionality through APIs
* Add observability
* Integrate with AWS services

## Progress

This repository will be updated as I progress through each module of the workshop.
