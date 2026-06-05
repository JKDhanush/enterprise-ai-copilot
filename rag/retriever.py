from rag.embeddings import get_embedding
from rag.vectordb import collection


def retrieve(query, k=2):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]