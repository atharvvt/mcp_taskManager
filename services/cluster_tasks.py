from services.embedding_service import embedding_from_json
import numpy as np
from sklearn.cluster import KMeans


def cluster_tasks(num_clusters=3):
    from database.operations import get_tasks
    tasks = get_tasks()

    valid_tasks = []
    embeddings = []

    for task in tasks:

        if not task[7]:
            continue

        valid_tasks.append(task)

        embeddings.append(
            embedding_from_json(task[7])
        )

    if len(valid_tasks) < num_clusters:
        num_clusters = len(valid_tasks)

    if num_clusters <= 0:
        return {}

    embeddings = np.array(embeddings)

    kmeans = KMeans(
        n_clusters=num_clusters,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(
        embeddings
    )

    clusters = {}

    for label, task in zip(
        labels,
        valid_tasks
    ):

        cluster_name = f"Cluster {label + 1}"

        if cluster_name not in clusters:
            clusters[cluster_name] = []

        clusters[cluster_name].append({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "priority": task[4]
        })

    return clusters