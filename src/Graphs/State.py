from typing import Any, TypedDict, Annotated
from langchain_core.documents import Document
from pydantic import BaseModel


# question: why to not use pydantic class here
class GraphState(TypedDict):
    """
    """
    documents:list[Document]
    webSearch: bool
    generation: str
    question: str
