import streamlit as st


def initialize_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_messages():

    for message in st.session_state.messages:

        if message["content"].startswith("Returned "):
            continue

        with st.chat_message(message["role"]):
            st.markdown(message["content"])