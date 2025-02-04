from agno.agent import Agent
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.youtube import YouTubeKnowledgeBase
from agno.models.google import Gemini
from agno.vectordb.pgvector import PgVector, SearchType
from dotenv import load_dotenv

load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
# Create a knowledge base of PDFs from URLs
knowledge_base = YouTubeKnowledgeBase(
    urls=["https://www.youtube.com/watch?v=pTB0EiLXUC8"],
    # Use PgVector as the vector database and store embeddings in the `ai.recipes` table
    vector_db=PgVector(
        table_name="youtubevideos",
        db_url=db_url,
        search_type=SearchType.hybrid,
        embedder=GeminiEmbedder(dimensions=768),
    ),
)
# Load the knowledge base: Comment after first run as the knowledge base is already loaded
knowledge_base.load(upsert=True)

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    knowledge=knowledge_base,
    # Enable RAG by adding context from the `knowledge` to the user prompt
    add_references=True,
    # Set as False because Agents default to `search_knowledge=True`
    search_knowledge=False,
    markdown=True,
)
agent.print_response(
    "Tell Detailed summary with timestamps for the video.", stream=True
)
