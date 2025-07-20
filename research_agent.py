# research_agent.py

import os
import asyncio
from llama_index.llms.google_genai import GoogleGenAI
from google.genai import types
from llama_index.core.workflow import Context
from llama_index.core.agent.workflow import (
    AgentWorkflow, FunctionAgent, AgentInput,
    AgentOutput, ToolCall, ToolCallResult
)

# Set your Gemini API Key
os.environ["GOOGLE_API_KEY"] = "your_gemini_api_key_here"

# LLM with search tool setup
google_search_tool = types.Tool(google_search=types.GoogleSearch())
llm_with_search = GoogleGenAI(
    model="gemini-2.5-pro",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
llm = GoogleGenAI(model="gemini-2.5-pro")

# Define tools
async def search_web(ctx: Context, query: str) -> str:
    response = await llm_with_search.acomplete(f"""Please research given this query:
    <query_or_topic>{query}</query_or_topic>""")
    return response

async def record_notes(ctx: Context, notes: str, notes_title: str) -> str:
    current_state = await ctx.store.get("state")
    current_state.setdefault("research_notes", {})
    current_state["research_notes"][notes_title] = notes
    await ctx.store.set("state", current_state)
    return "Notes recorded."

async def write_report(ctx: Context, report_content: str) -> str:
    current_state = await ctx.store.get("state")
    current_state["report_content"] = report_content
    await ctx.store.set("state", current_state)
    return "Report written."

async def review_report(ctx: Context, review: str) -> str:
    current_state = await ctx.store.get("state")
    current_state["review"] = review
    await ctx.store.set("state", current_state)
    return "Report reviewed."

# Define Agents
research_agent = FunctionAgent(
    name="ResearchAgent",
    description="Searches and records research notes.",
    system_prompt="You are the ResearchAgent...",
    llm=llm,
    tools=[search_web, record_notes],
    can_handoff_to=["WriteAgent"]
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Writes reports from research.",
    system_prompt="You are the WriteAgent...",
    llm=llm,
    tools=[write_report],
    can_handoff_to=["ReviewAgent"]
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Reviews and provides feedback.",
    system_prompt="You are the ReviewAgent...",
    llm=llm,
    tools=[review_report],
    can_handoff_to=["WriteAgent"]
)

# Build Workflow
agent_workflow = AgentWorkflow(
    agents=[research_agent, write_agent, review_agent],
    root_agent=research_agent.name,
    initial_state={
        "research_notes": {},
        "report_content": "Not written yet.",
        "review": "Review required."
    }
)

# Run the workflow
async def run_workflow():
    research_topic = """Write me a report on the history of the web."""
    handler = agent_workflow.run(user_msg=research_topic)
    current_agent = None

    async for event in handler.stream_events():
        if hasattr(event, "current_agent_name") and event.current_agent_name != current_agent:
            current_agent = event.current_agent_name
            print(f"\n{'='*50}\n🤖 Agent: {current_agent}\n{'='*50}\n")
        elif isinstance(event, AgentOutput):
            if event.response.content:
                print("📤 Output:", event.response.content)
            if event.tool_calls:
                print("🛠️ Planning tools:", [call.tool_name for call in event.tool_calls])
        elif isinstance(event, ToolCall):
            print(f"🔨 Tool: {event.tool_name} | Args: {event.tool_kwargs}")
        elif isinstance(event, ToolCallResult):
            print(f"✅ Tool Result: {event.tool_output}")

    # Final output
    state = await handler.ctx.store.get("state")
    print("\nFinal Report:\n", state["report_content"])
    print("\nReview:\n", state["review"])

if __name__ == "__main__":
    asyncio.run(run_workflow())
