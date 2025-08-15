# agents/analysis_agents.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def create_analysis_agent():
    """ 
    This is our main "thinking" agent. 
    It will now execute specific tasks based on the user's query.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4, google_api_key=os.getenv("GEMINI_API_KEY_AGENT1"))
    
    prompt_template = """
    You are an expert basketball analyst. Based on the data summary below, perform the requested task precisely.

    Data Summary:
    {data_summary}

    Requested Task:
    {query}

    Generate a response that directly answers the requested task. Use Markdown for formatting (e.g., bullet points and bold text).
    """
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["data_summary", "query"])
    return LLMChain(llm=llm, prompt=prompt, verbose=True)


def create_reporting_agent():
    """ 
    This agent formats the raw analysis into a clean, professional report.
    No changes needed here.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=os.getenv("GEMINI_API_KEY_AGENT2"))
    
    prompt_template = """
    You are an expert assistant coach. Your head coach is busy and needs a clear, concise summary.
    Convert the following raw analysis into a professional, easy-to-read report.
    Use headings and simple language. Address the coach directly.

    Raw Analysis:
    {analysis_output}

    Generate a final report.
    """
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["analysis_output"])
    return LLMChain(llm=llm, prompt=prompt, verbose=True)