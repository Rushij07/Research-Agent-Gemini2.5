# Research Agent using Gemini 2.5 Pro & LlamaIndex

A multi-agent research assistant built using Google Gemini 2.5 Pro and LlamaIndex. This system automates the research workflow by performing web searches, recording notes, writing structured reports, and reviewing the results. All tasks are orchestrated using LLMs and modular agent workflows.

## Features

- Web search using the integrated Google Search Tool
- Notes recording and persistent context state
- Automated report generation based on collected data
- Feedback loop for reviewing and refining the report
- Multi-agent collaboration and streaming execution

## Tech Stack

- LLM: Google Gemini 2.5 Pro
- Framework: LlamaIndex (Multi-Agent Workflows)
- Tools: Google Search Tool
- Language: Python 3.10+

## Installation

Clone the repository and install dependencies:
set GOOGLE_API_KEY=your_api_key


## Deployment Options

This project can be deployed using multiple approaches:

| Platform    | Method               | Notes                                        |
|-------------|----------------------|----------------------------------------------|
| Streamlit   | Wrap with a UI       | For real-time interaction via web interface  |
| FastAPI     | Expose REST API      | Best for backend service integration         |
| Docker      | Containerize         | Easily deployable on any cloud or server     |
| GCP / AWS   | Cloud Run / Lambda   | Scalable, serverless deployment options      |

## Monitoring and Scaling

- Add detailed logging to track agent actions and outputs.
- Integrate Prometheus and Grafana for performance monitoring.
- Use Docker for containerization.
- Scale using Kubernetes for distributed workloads.
- Add retry and error-handling mechanisms for stability and resilience.

## Example Use Case

**Prompt**:  
Write me a report on the history of the web.

**Workflow**:
1. The ResearchAgent searches the web and gathers information.
2. The WriteAgent generates a structured markdown report.
3. The ReviewAgent evaluates and suggests improvements or approves the report.

## Author

Rushikesh Jadhav  

