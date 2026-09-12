# Issues & Resolutions

This file documents the issues encountered while implementing the Strands MCP travel agent and the steps taken to resolve them.

---

## 1. `os` Not Defined

### Error

```text
NameError: name 'os' is not defined
```

### Cause

`os.environ` was used to read Lambda environment variables, but the `os` module was not imported.

### Resolution

Added:

```python
import os
```

---

## 2. MCP Client Initialization Failed

### Error

```text
MCPClientInitializationError:
the client initialization failed
```

### Cause

The AgentCore Gateway was using MCP protocol version `2025-11-25`, while the `strands:2` Lambda layer was using an older MCP client version.

### Resolution

Updated the AgentCore Gateway's supported MCP protocol versions by adding the **previous/older supported protocol version**.

After this change, the MCP client initialized successfully.

---

## 3. MCP Gateway Returned No Tools

### Error / Log

```text
Found the following tools: []
```

### Cause

The Gateway target configuration was not correctly exposing the Travel Attractions Lambda tools.

### Resolution

Updated the AgentCore Gateway target configuration and verified that the target exposed:

```text
list_attractions
reserve_ticket
cancel_ticket
```

After the update:

```text
Found the following tools:
[
  'target-quick-start-r4ashc___cancel_ticket',
  'target-quick-start-r4ashc___list_attractions',
  'target-quick-start-r4ashc___reserve_ticket'
]
```

---

## 4. Lambda Timed Out During Tool Execution

### Error

```text
Status: timeout
Duration: 60000.00 ms
```

### Cause

The agent repeatedly selected the `http_request` tool instead of the MCP `reserve_ticket` tool.

Example:

```text
Tool #1: http_request
Tool #2: http_request
Tool #3: http_request
...
```

This caused the Lambda to continue making tool calls until the 60-second timeout.

### Resolution

Temporarily removed `http_request` from the tool list to isolate the problem:

```python
tools_mcp += [flight_search, current_time]
```

This helped identify the subsequent tool-use issue.

---

## 5. Nova `Invalid Sequence as Part of ToolUse`

### Error

```text
modelStreamErrorException:
Model produced invalid sequence as part of ToolUse
```

### Cause

The MCP Gateway target name resulted in generated tool names containing hyphens, for example:

```text
target-quick-start-r4ashc___reserve_ticket
```

This caused an invalid tool-use sequence with the Nova model.

### Resolution

Renamed/recreated the Gateway target using an alphanumeric-only name without hyphens.

After updating the target, the MCP tools were exposed with valid tool names and Nova successfully selected the reservation tool.

---

## Final Result

After resolving the above issues:

```text
MCP Client                  ✅
AgentCore Gateway           ✅
MCP Tool Discovery          ✅
list_attractions            ✅
reserve_ticket              ✅
cancel_ticket               ✅
Flight Search               ✅
Weather Tool                ✅
Ticket Reservation          ✅
```

The travel agent successfully completed the **Space Needle ticket reservation** through the MCP Gateway.
