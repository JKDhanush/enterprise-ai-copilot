import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("⚙️ Settings")

        provider = st.selectbox(
            "LLM Provider",
            [
                "openrouter",
                "groq"
            ]
        )

        uploaded_file = st.file_uploader(
            "Upload Document",
            type=["pdf", "docx"]
        )

        st.divider()

        if st.button(
            "🗑️ Clear Chat",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.rerun()

    return provider, uploaded_file