import chromadb
import streamlit as st

from rag.embeddings import get_embedding


@st.cache_resource
def get_client():

    return chromadb.EphemeralClient()


def get_collection():

    client = get_client()

    return client.get_or_create_collection(
        name="documents"
    )


def store_chunks(chunks):

    client = get_client()

    try:

        client.delete_collection(
            name="documents"
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

    print(
        "COLLECTION COUNT:",
        collection.count()
    )