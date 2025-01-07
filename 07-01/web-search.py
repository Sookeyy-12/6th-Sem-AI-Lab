from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from dotenv import load_dotenv
import sys

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,      
)
web_agent.print_response("Who is Suket Kamboj", stream=True)