from typing import TypedDict, Any


class GraphState(TypedDict):
    question: str
    route: str
    response: str

    sql_result: Any
    sql_query: str

    document_loaded: bool