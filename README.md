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