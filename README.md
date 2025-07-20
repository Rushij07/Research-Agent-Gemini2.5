# 🤖 Research Agent using Gemini 2.5 Pro & LlamaIndex

A multi-agent research assistant powered by Google Gemini 2.5 Pro and LlamaIndex. This agent searches the web, stores notes, writes a report, and reviews it — all automatically through LLMs.

Features
Web search with Google Search Tool
Note recording and state storage
Report generation using research data
Review feedback cycle
Multi-agent handoff and streaming execution

Tech Stack

- LLM: Google Gemini 2.5 Pro
- Framework: LlamaIndex (Multi-agent Workflows)
- Tools: Google Search Tool
- Language: Python 3.10+

Installation
git clone https://github.com/yourusername/research-agent-llama.git
cd research-agent-llama
pip install -r requirements.txt

Set Your Gemini API Key
export GOOGLE_API_KEY="your_api_key"
On Windows CMD:
set GOOGLE_API_KEY=your_api_key
Run Locally

python research_agent.py
Deployment Options
Platform	Method	Notes
Streamlit	Wrap with a UI	Real-time input/output via web UI
FastAPI	Expose as REST API	Suitable for integration in apps
Docker	Containerize	Easier deployment to any cloud
GCP/AWS	Cloud Run/Lambda	For real-time scaling and monitoring

Monitoring & Scaling
Use logging in run_workflow() for detailed tracking.
Integrate with Prometheus + Grafana for performance insights.
To cale: Dockerize the app and use Kubernetes for orchestration.
Add retries and error handling to ensure robust workflows.

Example Use Case
Topic: Write me a report on the history of the web.
Agents will:
Search and collect research
Write a report
Review and finalize output

Author
Rushikesh Jadhav 
