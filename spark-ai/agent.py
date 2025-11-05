from google.adk.agents import Agent

root_agent = Agent(
    name="spark-ai",
    model="gemini-2.0-flash",
    description="Agent to answer questions about Costa Rica and its culture",
    instruction="You are a helpful agent who can answer user questions about Costa Rica and its culture",
)
