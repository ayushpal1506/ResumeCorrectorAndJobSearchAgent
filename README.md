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


## 🛠️ Installation & Setup

This project uses **CrewAI**, **LangChain**, and **TensorFlow**. Due to cross-dependency tracking rules within deep learning frameworks (especially on Apple Silicon M-series chips), please follow these setup instructions carefully.

### 📋 Prerequisites

* **Python Version:** **Python 3.12** is highly recommended. 
  * *Note:* Avoid Python 3.13 for now, as several core underlying ML libraries (like older PyArrow and TensorFlow dependencies) will fail to compile from source.
* **Operating System:** macOS (Intel/Apple Silicon), Linux, or Windows.


⚙️ Installation
1️⃣ Clone the repository
    git clone https://github.com/ayushpal1506/ResumeCorrectorAndJobSearchAgent.git
    cd ResumeCorrectorAndJobSearchAgent

2. Create a Python 3.12 Virtual Environment
Ensure you are explicitly targeting Python 3.12 when creating your environment sandbox:
On macOS / Linux:
Bash
# If python3.12 isn't your default, point directly to its binary path
python3.12 -m venv venv

source venv/bin/activate

On Windows:
Bash
python -m venv venv

.\venv\Scripts\activate

Upgrade Core Build Tools
Before installing the requirements, update your environment's packaging tools to ensure smoother wheel compilations:
Bash
pip install --upgrade pip setuptools wheel

3️⃣ Install dependencies

pip install -r requirements.txt --use-deprecated=legacy-resolver

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

