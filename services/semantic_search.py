from services.embedding_service import generate_embedding
from services.faiss_service import get_task_ids, search_faiss


def semantic_search(
    query,
    top_k=5
):
    from database.operations import get_tasks
    query_embedding = generate_embedding(
        query
    )

    scores, indices = search_faiss(
        query_embedding,
        top_k
    )

    tasks = get_tasks()

    task_lookup = {
        task[0]: task
        for task in tasks
    }

    task_ids = get_task_ids()

    results = []

    for score, idx in zip(
        scores,
        indices
    ):

        if idx < 0:
            continue

        if idx >= len(task_ids):
            continue

        task_id = task_ids[idx]

        task = task_lookup.get(
            task_id
        )

        if not task:
            continue

        results.append(
            (
                float(score),
                task
            )
        )

    return results