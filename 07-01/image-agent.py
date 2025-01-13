from phi.agent import Agent
from phi.model.google import Gemini
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=True,
)

agent.print_response(
    "What are in these images? Is there any difference between them?",
    images=[
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
    ],
)
