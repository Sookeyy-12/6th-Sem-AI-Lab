from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[DuckDuckGo()],
    instructions=["Use DuckDuckGo for searching on the web. Search on the web for each user query."],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Who is the Prime minister of India as of 2025")