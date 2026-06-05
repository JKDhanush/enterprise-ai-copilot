from rag.embeddings import get_embedding
from rag.vectordb import get_collection


def retrieve(query, k=2):

    collection = get_collection()

    query_embedding = get_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]