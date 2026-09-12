from strands import Agent, tool
from typing import Dict, Any

# Define a travel-focused system prompt
TRAVEL_AGENT_PROMPT = """
You are a travel assistant that can help customers book their travel.

Think step-by-step. Limit your anwers to the user prompt.

Tools available:
- Use the flight_search tool to provide flight carrier choices for their destination.
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
    travel_agent = Agent(
        model="amazon.nova-lite-v1:0",
        system_prompt=TRAVEL_AGENT_PROMPT,
        tools=[flight_search]
    )
    response = travel_agent(event.get('prompt'))
    return str(response)