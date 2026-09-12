from strands import Agent, tool
from strands_tools import http_request
from strands.session.s3_session_manager import S3SessionManager
from typing import Dict, Any
import boto3
import os
import json

# Define a travel-focused system prompt
TRAVEL_AGENT_PROMPT = """
You are a travel assistant that can help customers book their travel.

Think step-by-step. Limit your anwers to the user prompt.

Tools available:
- Use the flight_search tool to provide flight carrier choices for their destination.

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
            "Southwest Airlines"
        ],
        "London": [
            "British Airways",
            "Virgin Atlantic"
        ],
        "Tokyo": [
            "Japan Airlines",
            "ANA"
        ]
    }
    return flights.get(city, [])

    
# The handler function

def handler(event: Dict[str, Any], _context) -> str:
    session_manager = S3SessionManager(
        session_id=event["user"]["session_id"],
        bucket=os.environ['SESSIONS_BUCKET'],
        prefix="agent-sessions"
    )
    travel_agent = Agent(
        model="amazon.nova-lite-v1:0",
        system_prompt=TRAVEL_AGENT_PROMPT,
        tools=[flight_search, http_request],
        session_manager=session_manager
    )
    response = travel_agent(event.get('prompt'))
    # return str(response)
    return response.message['content'][0]['text']