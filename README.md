# Multi tool AI Agent

A powerful AI agent built with LangChain and LangGraph that can perform web searches, get weather information, and provide intelligent responses using OpenAI's GPT-4o-mini model.

## Features

- **Web Search Integration**: Uses Tavily Search API for real-time web search capabilities
- **Weather Information**: Get current weather data for any city using OpenWeatherMap API
- **Memory Persistence**: Maintains conversation context across interactions using thread-based memory
- **ReAct Agent**: Implements the ReAct (Reasoning + Acting) pattern for better decision making
- **OpenAI GPT-4o-mini**: Powered by OpenAI's latest language model
- **Multi-tool Support**: Automatically chooses between search and weather tools based on user queries

## Prerequisites

- Python 3.8+
- OpenAI API key
- Tavily Search API key
- OpenWeatherMap API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pkarcreative/search_ai_agent.git
cd search_ai_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables by creating a `.env` file:
```bash
# Required API Keys
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHER_API_KEY=your_openweather_api_key

# Optional Configuration
OPENAI_MODEL=gpt-4o-mini
TAVILY_MAX_RESULTS=2
ENVIRONMENT=development
```

## API Keys Setup

### OpenAI API Key
1. Sign up at [platform.openai.com](https://platform.openai.com)
2. Generate an API key in your account settings
3. Add it to your `.env` file

### Tavily Search API Key
1. Sign up at [tavily.com](https://tavily.com)
2. Get your API key from the dashboard
3. Add it to your `.env` file

### OpenWeatherMap API Key
1. Sign up at [openweathermap.org/api](https://openweathermap.org/api)
2. Generate a free API key (1,000 calls/day)
3. **Note**: New API keys take 2-4 hours to activate
4. Add it to your `.env` file

## Usage

```python
from search_agent import agent_executor

# Configure the agent with a unique thread ID
config = {"configurable": {"thread_id": "user123"}}

# Ask for weather information
input_message = {
    "role": "user",
    "content": "What's the weather in Melbourne, Australia?"
}

# Stream the agent's response
for step in agent_executor.stream(
    {"messages": [input_message]}, 
    config, 
    stream_mode="values"
):
    step["messages"][-1].pretty_print()
```

## Example Queries

The agent can handle various types of requests:

- **Weather queries**: "What's the weather in Tokyo?"
- **Web searches**: "What are the latest developments in AI?"
- **Combined requests**: "Search for information about climate change and tell me the weather in New York"

## Project Structure

```
search_ai_agent/
├── search_agent.py    # Main agent implementation with weather and search tools
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (not tracked by Git)
├── .env.example      # Example environment file template
└── README.md         # This file
```

## Dependencies

- `langchain>=0.1.0` - LangChain framework
- `langchain-tavily>=0.1.0` - Tavily search integration
- `langchain-openai>=0.1.0` - OpenAI integration
- `langgraph>=0.0.20` - LangGraph for stateful AI applications
- `python-dotenv>=1.0.0` - Environment variable management
- `requests>=2.31.0` - HTTP requests for weather API

## Features in Detail

### Weather Tool
- **Free API**: OpenWeatherMap with 1,000 calls/day
- **Global coverage**: Works with any city worldwide
- **Rich data**: Temperature, humidity, wind speed, conditions
- **Error handling**: Graceful fallbacks for API issues

### Search Tool
- **Real-time results**: Latest information from the web
- **Configurable results**: Adjustable number of search results
- **Intelligent filtering**: AI-powered result selection

### Memory System
- **Thread-based**: Each conversation gets a unique thread ID
- **Persistent context**: Maintains conversation history
- **Multi-user support**: Separate conversations for different users

## Troubleshooting

### Weather API Issues
- **401 Unauthorized**: API key not activated yet (wait 2-4 hours)
- **City not found**: Check city spelling and try alternative names
- **Rate limit exceeded**: Free tier allows 1,000 calls/day

### General Issues
- **Missing API keys**: Ensure all required keys are in your `.env` file
- **Import errors**: Run `pip install -r requirements.txt`
- **Memory issues**: Each thread maintains separate conversation history

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues:
1. Check that all API keys are properly set in your `.env` file
2. Verify that dependencies are installed correctly
3. Ensure your API keys are active and have sufficient quota
4. Check the troubleshooting section above
