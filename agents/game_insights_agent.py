# agents/game_insights_agent.py

import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType

load_dotenv()

def game_insights_agent(logs):
    time.sleep(1.5)

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GEMINI_API_KEY_AGENT1")
    )

    tools = load_tools(["wikipedia"], llm=llm)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    prompt = f"""
You are a basketball game insights agent.

From the following logs, do two things:
1. Extract structured stats:
   - Which team won
   - Total fast break points
   - Total 3-pointers
   - Final score summary

2. Analyze player performance:
   - Who stood out (good or bad)
   - Any standout plays or patterns

Logs:
{logs}

Respond with:
📊 Game Summary
🧠 Player Performance Insights
"""

    return agent.run(prompt)
