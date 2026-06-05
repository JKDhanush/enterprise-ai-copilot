from agents.router_agent import (
    route_question
)

questions = [

    "Summarize my resume",

    "Show top customers by revenue",

    "What is LangGraph?"
]

for q in questions:

    print(q)

    print(
        route_question(q)
    )

    print("-" * 50)