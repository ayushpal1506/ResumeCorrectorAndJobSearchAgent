# ResumeCorrectorAndJobSearchAgent


An AI-powered multi-agent system that analyzes resumes, identifies missing skills/ATS gaps, and searches for matching internships or entry-level software engineering opportunities.

Built using:

* CrewAI￼
* LangGraph￼
* Anthropic Claude￼
* LangChain Community￼

⸻

🚀 Features

📄 Resume Analysis Agent

* Reads resume PDFs
* Detects:
    * missing technical skills
    * ATS keyword gaps
    * project weaknesses
    * formatting improvements
* Provides actionable recommendations

🔍 Job Search Agent

* Searches for:
    * internships
    * entry-level software engineering roles
* Returns:
    * company name
    * role title
    * direct application link

🤖 Multi-Agent Workflow

Uses a sequential AI workflow:

1. Resume Analysis
2. User Feedback/Input
3. Job Search Recommendations

Powered by LangGraph state management.

⸻

🛠️ Tech Stack



Technology      |    Purpose

Python          |   Core programming language

CrewAI          |    Multi-agent orchestration

LangGraph       |   Workflow management

Claude Haiku    |   LLM reasoning

SerperDevTool   |    Web job search

PyPDFLoader     |   Resume PDF parsing



📂 Project Structure

ResumeCorrectorAndJobSearchAgent/
│
├── script.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env


⚙️ Installation
1️⃣ Clone the repository
    git clone https://github.com/ayushpal1506/ResumeCorrectorAndJobSearchAgent.git
    cd ResumeCorrectorAndJobSearchAgent

2️⃣ Create virtual environment
    python -m venv venv

Activate it:
        Mac/Linux: source venv/bin/activate
        Windows : venv\Scripts\activate
3️⃣ Install dependencies

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file:
ANTHROPIC_API_KEY=your_api_key_here  || or any llm of your choice
SERPER_API_KEY=your_serper_api_key_here

▶️ Running the Project
Update the resume path inside script.py:
    resume_path = "your_resume.pdf"

Then run:
python script.py

🧠 Workflow Architecture
Resume PDF
    ↓
Resume Analysis Agent
    ↓
Improvement Suggestions
    ↓
User Input
    ↓
Job Search Agent
    ↓
Top Matching Opportunities

