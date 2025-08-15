# Search AI Agent

A powerful AI agent built with LangChain and LangGraph that can perform web searches and provide intelligent responses using Claude 3.5 Sonnet.

## Features

- **Web Search Integration**: Uses Tavily Search API for real-time web search capabilities
- **Memory Persistence**: Maintains conversation context across interactions
- **ReAct Agent**: Implements the ReAct (Reasoning + Acting) pattern for better decision making
- **Claude 3.5 Sonnet**: Powered by Anthropic's latest language model

## Prerequisites

- Python 3.8+
- Anthropic API key
- Tavily Search API key

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

3. Set up environment variables:
```bash
export ANTHROPIC_API_KEY="your_anthropic_api_key"
export TAVILY_API_KEY="your_tavily_api_key"
```

## Usage

```python
from aearch_agent import agent_executor

# Run the agent with a query
response = agent_executor.invoke({"input": "What are the latest developments in AI?"})
print(response)
```

## Project Structure

```
search_ai_agent/
├── aearch_agent.py    # Main agent implementation
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Dependencies

- langchain
- langchain-tavily
- langgraph
- anthropic

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
