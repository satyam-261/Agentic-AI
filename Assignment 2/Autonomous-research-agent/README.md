# Autonomous Research Agent

## How to Run

1. Install requirements:
pip install -r requirements.txt

2. Add .env with your OpenAI API key

3. Run:
python main.py

## Features
- Autonomous Research using LangChain
- Uses Zero-Shot ReAct Agent
- Web Search Tool (DuckDuckGo)
- Knowledge Tool (Wikipedia)
- Structured Report Generation

## Agent Workflow
1. Takes topic input
2. Uses tools to gather data
3. Analyzes information
4. Generates structured report

## Sample Topics
- Impact of AI in Healthcare
- Blockchain in Finance

## Agent Type
This project uses a Zero-Shot ReAct Agent for autonomous reasoning and tool usage.

## Note
This project requires an OpenAI API key to run.

Set it using:
export OPENAI_API_KEY=your_key

Or inside code using:
os.environ["OPENAI_API_KEY"] = "your_key"
