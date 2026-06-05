import chromadb

from rag.embeddings import get_embedding


client = chromadb.EphemeralClient()

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks):

    global collection

    try:

        client.delete_collection(
            "documents"
        )

    except:
        pass

    collection = client.get_or_create_collection(
        name="documents"
    )

    for idx, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[chunk]
        )