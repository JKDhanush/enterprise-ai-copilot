import chromadb

from rag.embeddings import get_embedding


client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_or_create_collection(
    name="documents"
)


def clear_collection():

    existing = collection.get()

    if existing["ids"]:

        collection.delete(
            ids=existing["ids"]
        )


def store_chunks(chunks):

    clear_collection()

    for idx, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[chunk]
        )