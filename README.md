# LangGraph Agentic RAG

An advanced RAG application built with LangGraph that combines Adaptive RAG, Corrective RAG (CRAG), and Self-RAG patterns to improve document retrieval, web search, answer grounding, and response quality.

## Tech Stack

- Python
- LangGraph
- LangChain
- OpenAI
- ChromaDB
- Tavily
- RAG
- Adaptive RAG
- Corrective RAG (CRAG)
- Self-RAG

## .env Requirement

OPENAI_API_KEY,
LANGSMITH_TRACING=true,
LANGSMITH_API_KEY,
LANGSMITH_PROJECT,
PYTHONPATH,
PINECONE_API_KEY.

## document ingestion

Web Articles
     │
     ▼
WebBaseLoader
     │
     ▼
Documents
     │
     ▼
RecursiveCharacterTextSplitter
chunk_size = 250
chunk_overlap = 0
     │
     ▼
OpenAIEmbeddings
     │
     ▼
ChromaDB
     │
     ▼
Retriever

## RAG Architecture

This project combines three advanced RAG patterns:

### Adaptive RAG
The system dynamically adapts its workflow based on the available information
and retrieval quality. It can choose between document retrieval and web search.

### Corrective RAG (CRAG)
Retrieved documents are graded for relevance. Irrelevant documents trigger
corrective actions such as web search.

### Self-RAG
Generated answers are evaluated for:

- Hallucinations
- Grounding in retrieved documents
- Relevance to the user's question

### RAG Flow

                         User Question
                              │
                              ▼
                       LangGraph Workflow
                              │
                              ▼
                       Retrieve Documents
                              │
                              ▼
                       Grade Documents
                              │
                 ┌────────────┴────────────┐
                 │                         │
            Relevant                  Not Relevant
                 │                         │
                 ▼                         ▼
            Generate                  Web Search
             Answer                       │
                 │                         │
                 │                    Retrieved Data
                 │                         │
                 └────────────┬────────────┘
                              ▼
                         Generate Answer
                              │
                              ▼
                       Evaluate Response
                              │
                 ┌────────────┴────────────┐
                 │                         │
              Grounded                 Not Grounded
                 │                         │
                 ▼                         ▼
              Answer                  Regenerate

### Langgraph

Question
   │
   ▼
Retrieve
   │
   ▼
Grade Documents
   │
   ├──────────────► Relevant ──────► Generate
   │
   └──────────────► Not Relevant ──► Web Search
                                      │
                                      ▼
                                   Generate
                                      │
                                      ▼
                              Evaluate Answer
                                      │
                                      ▼
                                   Response

### Run the Application

uv run main.py