from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=["Output only and only the code and nothing else."],
)

agent.print_response("Write a C code to print Hello World!")