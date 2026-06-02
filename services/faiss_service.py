import faiss
import numpy as np

from database.operations import get_tasks
from services.embedding_service import (
    embedding_from_json
)

index = None
task_ids = []

def build_faiss_index():

    global index
    global task_ids

    tasks = get_tasks()

    embeddings = []
    task_ids = []

    for task in tasks:

        if not task[7]:
            continue

        embeddings.append(
            embedding_from_json(task[7])
        )

        task_ids.append(task[0])

    if not embeddings:
        return False

    vectors = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    faiss.normalize_L2(vectors)

    index.add(vectors)

    return True

def search_faiss(
    query_embedding,
    top_k=5
):

    global index

    if index is None:
        build_faiss_index()

    query = np.array(
        [query_embedding],
        dtype="float32"
    )

    faiss.normalize_L2(query)

    scores, indices = index.search(
        query,
        top_k
    )

    return scores[0], indices[0]

def get_task_ids():
    return task_ids