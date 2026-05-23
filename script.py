import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

os.environ["OTEL_SDK_DISABLED"] = "true" # Disables the telemetry error


my_llm = LLM(
    model="claude-haiku-4-5-20251001",
    api_key=api_key
)


class AgentState(TypedDict):
    resume_text: str
    analysis_feedback: str
    user_input: str
    job_listings: str



def run_analysis_crew(state: AgentState):
    """Agent 1: Analyzes the resume for gaps and ATS optimization."""
    analyst = Agent(
        role='Senior Talent Acquisition Manager',
        goal='Identify missing technical skills and ATS gaps in the resume.',
        backstory='Expert in tech hiring and resume optimization for top-tier firms.',
        llm=my_llm,
        verbose=True,
        allow_delegation=False
    )
    
    task = Task(
        description=(
            f"Review this resume text: {state['resume_text']}. "
            "Identify what is missing for a Master of Computer Applications (MCA) student "
            "aiming for high-frequency trading or software engineering roles. "
            "Focus on missing keywords, project gaps, or formatting issues."
        ),
        expected_output="A bulleted list of 3-5 specific missing items or improvements.",
        agent=analyst
    )
    
    result = Crew(agents=[analyst], tasks=[task]).kickoff()
    return {"analysis_feedback": str(result)}

from crewai_tools import SerperDevTool

def run_job_search_crew(state: AgentState):

    

    search_tool = SerperDevTool()

    scout = Agent(
        role='Career Opportunity Scout',
        goal='Find exactly 5 active internship links matching the user profile.',
        backstory='Expert in finding technical roles on the web.',
        tools=[search_tool], 
        llm=my_llm, 
        verbose=True,
        allow_delegation=False
    )
    
    task = Task(
        description=(
            f"Search for 5 internships/entry-level jobs in India for these skills: {state['resume_text']}. "
            f"User input: {state['user_input']}. "
            "You MUST provide: 1. Company Name, 2. Role Title, 3. A direct Link to apply."
        ),
        expected_output="A list of 5 active job titles, companies, and URLs.",
        agent=scout
    )
    
    result = Crew(agents=[scout], tasks=[task]).kickoff()
    return {"job_listings": str(result)}

workflow = StateGraph(AgentState)

workflow.add_node("analyze_resume", run_analysis_crew)
workflow.add_node("search_jobs", run_job_search_crew)

workflow.set_entry_point("analyze_resume")
workflow.add_edge("analyze_resume", "search_jobs")
workflow.add_edge("search_jobs", END)

app = workflow.compile()


def start_app(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File not found at {pdf_path}")
        return


    print("\n--- 🧐 Step 1: Reading and Analyzing Resume... ---")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    resume_text = " ".join([p.page_content for p in pages])


    initial_state = {
        "resume_text": resume_text, 
        "user_input": "", 
        "analysis_feedback": "", 
        "job_listings": ""
    }
    analysis_output = run_analysis_crew(initial_state)
    
    print("\n" + "="*40)
    print("📋 AGENT FEEDBACK & RECOMMENDATIONS:")
    print(analysis_output['analysis_feedback'])
    print("="*40)
    

    user_resp = input("\n✍️ Enter missing info/skills (or 'none' to continue to search): ")
    

    print("\n--- 🔍 Step 2: Searching for Matching Opportunities... ---")
    final_state = {
        "resume_text": resume_text,
        "analysis_feedback": analysis_output['analysis_feedback'],
        "user_input": user_resp
    }
    job_output = run_job_search_crew(final_state)
    
    print("\n" + "🌟" * 20)
    print("🎯 TOP JOB MATCHES FOR YOU:")
    print(job_output['job_listings'])
    print("🌟" * 20)

if __name__ == "__main__":

    resume_path = "/Users/ayushpal/Desktop/AgenticAi/Ayush_Pal_Resume.pdf"
    start_app(resume_path)