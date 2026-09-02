from typing import Any

from graph.state import GraphState
from ingestion import retriever


def retrieve(state: GraphState) -> dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever.invoke(question)#do the semantic search
    return {"documents": documents, "question": question}