import chromadb

from rag.embeddings import get_embedding


client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks):

    try:

        existing = collection.get()

        if existing["ids"]:

            collection.delete(
                ids=existing["ids"]
            )

    except Exception:

        pass

    for idx, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[chunk]
        )