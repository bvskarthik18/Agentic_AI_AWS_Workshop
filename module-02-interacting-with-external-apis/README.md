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

### Changes Made in `index.py`

1. **Added HTTP request tool**

```python
from strands_tools import http_request
```

2. **Updated the system prompt**

   * Weather is provided only when explicitly requested.
   * Uses the **National Weather Service API**.
   * Fetches weather for Seattle.
   * Returns a 5-day summary with temperature, precipitation, and alerts.

3. **Added `http_request` to the agent tools**

```python
tools=[flight_search, http_request]
```

4. **Updated Lambda response handling**

Changed from:

```python
return str(response)
```

to:

```python
return response.message['content'][0]['text']
```

### What Remained Unchanged

* `flight_search` tool
* `amazon.nova-lite-v1:0` model
* Lambda handler structure


## Test Event

**Input**

```text
What's the weather forecast for Seattle?
```

### Result

The travel agent can now:

* Search available flight carriers.
* Fetch weather information from an external API when requested.
* Return a clean text response from Lambda.

## Key Learnings

* Added new functionality to an existing AI Agent
* Updated the agent's system prompt
* Used the `http_request` tool
* Interacted with an external API
* Updated and redeployed the Lambda function
