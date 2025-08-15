# router/agent_pipeline.py

import pandas as pd
from agents.analysis_agents import create_analysis_agent, create_reporting_agent

def run_agent_pipeline(query: str, csv_path: str):
    """
    This function orchestrates the entire agent workflow.
    """
    # Step 1: Data Extraction (Reading the CSV)
    try:
        df = pd.read_csv(csv_path)
        # Convert the last 20 games into a simple text summary for the agent
        data_summary = df.tail(20).to_string()
    except Exception as e:
        return {"error": f"Failed to read or process data: {str(e)}"}

    # Step 2: Call Analysis Agent (Agent 1)
    analysis_agent = create_analysis_agent()
    analysis_result = analysis_agent.invoke({"data_summary": data_summary, "query": query})
    analysis_output = analysis_result['text']
    
    # Step 3: Call Reporting Agent (Agent 2)
    reporting_agent = create_reporting_agent()
    reporting_result = reporting_agent.invoke({"analysis_output": analysis_output})
    final_report = reporting_result['text']
    
    # Step 4: Return the results in a structured dictionary
    return {
        "final_report": final_report,
        "raw_analysis": analysis_output, # We can use this for a "detailed view" if needed
    }