from services.embedding_service import cosine_similarity, embedding_from_json


def find_related_tasks(
    target_task,
    all_tasks,
    top_k=3
):
    if not target_task[7]:
        return []

    target_embedding = embedding_from_json(
        target_task[7]
    )

    results = []

    for task in all_tasks:

        if task[0] == target_task[0]:
            continue

        if not task[7]:
            continue

        task_embedding = embedding_from_json(
            task[7]
        )

        similarity = cosine_similarity(
            target_embedding,
            task_embedding
        )

        results.append(
            (similarity, task)
        )

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return results[:top_k]