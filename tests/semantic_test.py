from services.semantic_search import semantic_search

results = semantic_search(
    "AI infrastructure"
)

for score, task in results:

    print(
        f"{score:.4f}",
        task[1]
    )