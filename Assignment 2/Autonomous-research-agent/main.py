import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

search = DuckDuckGoSearchRun()
wiki = WikipediaAPIWrapper()

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Search the internet for current information"
    ),
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Get detailed knowledge from Wikipedia"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def generate_report(topic):
    prompt = f'''
You are an autonomous research agent.

Research the topic: "{topic}"

Format:

COVER PAGE
Title: {topic}

INTRODUCTION
Explain topic

KEY FINDINGS
Points

CHALLENGES
List

FUTURE SCOPE
Future

CONCLUSION
Summary
'''
    return agent.run(prompt)

if __name__ == "__main__":
    topic = input("Enter research topic: ")
    report = generate_report(topic)
    print(report)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)
