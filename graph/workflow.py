from langgraph.graph import StateGraph, END

from graph.state import GraphState

from agents.router_agent import route_question
from agents.sql_agent import answer_sql_question
from agents.rag_agent import answer_question

from llm.service import LLMService

llm = LLMService()


def router_node(state):

    route = route_question(
        state["question"]
    )

    return {
        **state,
        "route": route
    }


def sql_node(state):

    sql, result = answer_sql_question(
        state["question"]
    )

    return {
        **state,
        "response": f"📊 SQL Agent returned {len(result)} rows.",
        "sql_result": result,
        "sql_query": sql
    }


def rag_node(state):

    response = answer_question(
        state["question"]
    )

    return {
        **state,
        "response": response
    }


def general_node(state):

    response = llm.generate(
        [
            {
                "role": "user",
                "content": state["question"]
            }
        ],
        provider="groq"
    )

    return {
        **state,
        "response": response
    }


builder = StateGraph(GraphState)

builder.add_node(
    "router",
    router_node
)

builder.add_node(
    "sql",
    sql_node
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "general",
    general_node
)

builder.set_entry_point("router")


def route(state):

    return state["route"]


builder.add_conditional_edges(
    "router",
    route,
    {
        "sql": "sql",
        "rag": "rag",
        "general": "general"
    }
)

builder.add_edge("sql", END)
builder.add_edge("rag", END)
builder.add_edge("general", END)

graph = builder.compile()