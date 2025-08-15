# Import relevant functionality
import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool

# Load environment variables from .env file
load_dotenv()

# Get API keys and configuration from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
TAVILY_MAX_RESULTS = int(os.getenv("TAVILY_MAX_RESULTS", "2"))

print(OPENAI_API_KEY)
print(TAVILY_API_KEY)
print(OPENWEATHER_API_KEY)
print(OPENAI_MODEL)
print(TAVILY_MAX_RESULTS)

# Validate required API keys
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in environment variables")
if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in environment variables")

# Custom weather tool
@tool
def get_weather(city: str) -> str:
    """
    Get current weather information for a specific city.
    
    Args:
        city: The name of the city (e.g., "Melbourne", "New York", "London")
    
    Returns:
        A string containing current weather information for the city
    """
    try:
        # OpenWeatherMap API endpoint
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"  # Use Celsius
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract weather information
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        city_name = data["name"]
        country = data["sys"]["country"]
        
        weather_info = f"Current weather in {city_name}, {country}:\n"
        weather_info += f"🌡️ Temperature: {temperature}°C\n"
        weather_info += f"🌡️ Feels like: {feels_like}°C\n"
        weather_info += f"💧 Humidity: {humidity}%\n"
        weather_info += f"🌤️ Conditions: {description.capitalize()}\n"
        weather_info += f"💨 Wind Speed: {wind_speed} m/s"
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"
    except KeyError as e:
        return f"Error parsing weather data: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Create the agent
memory = MemorySaver()
model = ChatOpenAI(model=OPENAI_MODEL, api_key=OPENAI_API_KEY)
search = TavilySearch(max_results=TAVILY_MAX_RESULTS)
weather_tool = get_weather
tools = [search, weather_tool]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}
input_message = {
    "role": "user",
    "content": "I am going to Melbourne, AU tomorrow for basic female haircut. Suggest me several places to go and then respond the best time to go tomorrow.",
}

for step in agent_executor.stream(
    {"messages": [input_message]}, config, stream_mode="values"
):
    step["messages"][-1].pretty_print()