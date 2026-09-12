from strands import Agent, tool
from strands_tools import http_request, current_time
from strands.session.s3_session_manager import S3SessionManager
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from typing import Dict, Any
import os
import requests
import json
import re

THINKING_PATTERN = r'<thinking>.*?</thinking>'

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
TOKEN_URL = os.environ['DOMAIN_URL'] + '/oauth2/token'
GATEWAY_URL = os.environ['GATEWAY_URL']

# Define a travel-focused system prompt
TRAVEL_AGENT_PROMPT = """You are a travel assistant that can help customers book their travel.

Think step-by-step. Limit your answers to the user prompt.

Tools available:
- Use the flight_search tool to provide flight carrier choices for their destination.
- Use the retrieve tool to get validated list of tour operators for different kinds of tours and activities that we support.
- Use list_attractions, reserve_ticket and cancel_ticket tools to provide attractions management service.

Weather Forecast:
- ONLY provide weather forecast if the user explicitly asks for it.
- To fetch weather data, follow these steps strictly:
    1. Make HTTP requests to the National Weather Service API using ONLY GET method
    2. For Seattle: latitude 47.6061°N, longitude 122.3328°W
    3. Get grid info: https://api.weather.gov/points/{latitude},{longitude}
    4. Get forecast: use the returned forecast URL
    5. Provide ONLY a 5-day summary with key conditions (temperature, precipitation, alerts)
    6. Do NOT include detailed daily/nightly breakdowns or extended forecasts

    """

@tool
def flight_search(city: str) -> dict:
    """Get available flight options to a city.

    Args:
        city: The name of the city
    """
    flights = {
        "Atlanta": [
            "Delta Airlines",
            "Spirit Airlines"
        ],
        "Seattle": [
            "Alaska Airlines",
            "Delta Airlines"
        ],
        "New York": [
            "United Airlines",
            "JetBlue"
        ]
    }
    return flights[city]

def fetch_access_token(client_id, client_secret, token_url):
  response = requests.post(
    token_url,
    data="grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}".format(client_id=client_id, client_secret=client_secret),
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
  )
  return response.json()['access_token']

def create_streamable_http_transport(mcp_url: str, access_token: str):
       return streamablehttp_client(mcp_url, headers={"Authorization": f"Bearer {access_token}"})


# The handler function signature `def handler(event, context)` is what Lambda
# looks for when invoking your function.
def handler(event: Dict[str, Any], _context):

    try:
        # Parse API Gateway request body
        body = json.loads(event["body"]) if isinstance(event.get("body"), str) else event.get("body", event)

        # Get session ID
        session_id = body.get("user", {}).get("session_id", "api-test-session")

        session_manager = S3SessionManager(
            session_id=session_id,
            bucket=os.environ["SESSIONS_BUCKET"],
            prefix="agent-sessions"
        )

        access_token = fetch_access_token(
            CLIENT_ID,
            CLIENT_SECRET,
            TOKEN_URL
        )

        mcp_client = MCPClient(
            lambda: create_streamable_http_transport(
                GATEWAY_URL,
                access_token
            )
        )

        with mcp_client:
            tools_mcp = mcp_client.list_tools_sync()

            print(
                f"Found the following tools: "
                f"{[tool.tool_name for tool in tools_mcp]}"
            )

            tools_mcp += [
                flight_search,
                http_request,
                current_time
            ]

            travel_agent = Agent(
                model="us.amazon.nova-lite-v1:0",
                system_prompt=TRAVEL_AGENT_PROMPT,
                tools=tools_mcp,
                session_manager=session_manager
            )

            response = travel_agent(body["prompt"])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "response": re.sub(
                    THINKING_PATTERN,
                    "",
                    str(response),
                    flags=re.DOTALL
                ).strip()
            })
        }

    except Exception as e:
        print(f"An error occurred: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }