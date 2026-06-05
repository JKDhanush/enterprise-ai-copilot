import chromadb

from rag.embeddings import get_embedding


client = chromadb.EphemeralClient()


def get_collection():

    return client.get_or_create_collection(
        name="documents"
    )


def store_chunks(chunks):

    try:

        client.delete_collection(
            name="documents"
        )

    except:
        pass

    collection = get_collection()

    for idx, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[chunk]
        )