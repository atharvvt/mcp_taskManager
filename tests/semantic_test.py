from services.embedding_service import semantic_search

results = semantic_search(
    "AI infrastructure"
)

for score, task in results:

    print(
        f"{score:.4f}",
        task[1]
    )