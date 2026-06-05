import chromadb

from rag.embeddings import get_embedding


client = chromadb.Client()

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

    except:
        pass

    for idx, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.upsert(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[chunk]
        )