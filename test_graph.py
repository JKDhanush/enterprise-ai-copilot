from graph.workflow import graph

result = graph.invoke(
    {
        "question": "Show top customers by revenue"
    }
)

print(result)