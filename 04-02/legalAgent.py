from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.pgvector import PgVector
from knowledge_base import knowledge_base
from agno.models.google import Gemini

pdf_knowledge_base = PDFKnowledgeBase(
    path="04-02\\basic-laws-book-2016.pdf",
    # Table name: ai.pdf_documents
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
    reader=PDFReader(chunk=True),
)

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    knowledge_base=knowledge_base,
    search_knowledge=True,
    markdown=True,
)

agent.knowledge.load(recreate=False)

agent.print_response("Tell me some basic laws.")