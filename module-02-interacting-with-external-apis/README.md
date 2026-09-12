# Module 2 — Interacting with External APIs

## Overview

Updated the Travel Agent to add new functionality and interact with an external API.

## What I Built

* Added weather forecast functionality
* Updated the system prompt with weather instructions
* Added the `http_request` tool
* Integrated with the **National Weather Service API**
* Updated and deployed `index.py` to AWS Lambda
* Tested the agent with a Seattle weather request

## Architecture

```text
User Prompt
    ↓
AWS Lambda
    ↓
Strands Agent
    ↓
http_request Tool
    ↓
National Weather Service API
    ↓
Weather Forecast
```

## Example

**Input**

```text
What's the weather forecast for Seattle?
```

**Result**

The agent successfully retrieved and returned the weather forecast for Seattle.

## Key Learnings

* Added new functionality to an existing AI Agent
* Updated the agent's system prompt
* Used the `http_request` tool
* Interacted with an external API
* Updated and redeployed the Lambda function
