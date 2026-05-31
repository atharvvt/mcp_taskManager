import json
from sentence_transformers import SentenceTransformer
from numpy import dot, array
from numpy.linalg import norm

MIN_SIMILARITY = 0.15

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def generate_embedding(text: str):
    vector = model.encode(text)
    return vector.tolist()

def embedding_to_json(vector):
    return json.dumps(vector)

def embedding_from_json(text):
    return json.loads(text)

def cosine_similarity(vec1, vec2):
    vec1 = array(vec1)
    vec2 = array(vec2)

    return dot(vec1, vec2) / (
        norm(vec1) * norm(vec2)
    )

def semantic_search(tasks, query, top_k=5):

    query_embedding = generate_embedding(query)

    results = []

    for task in tasks:

        if not task[7]:
            continue

        task_embedding = embedding_from_json(task[7])

        similarity = cosine_similarity(
            query_embedding,
            task_embedding
        )

        if similarity >= MIN_SIMILARITY:
            results.append((similarity, task))

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return results[:top_k]