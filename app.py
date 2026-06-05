import os
import streamlit as st

from frontend.chat_ui import (
    initialize_chat,
    display_messages
)

from frontend.sidebar import render_sidebar

from llm.service import LLMService

from rag.loader import (
    load_pdf,
    load_docx
)

from agents.router_agent import route_question

from agents.sql_agent import (
    answer_sql_question
)

from rag.chunker import chunk_text
from rag.vectordb import store_chunks
from agents.rag_agent import answer_question
from graph.workflow import graph
from database.db import run_query

import tempfile

from voice.transcriber import (
    transcribe_audio
)

from voice.analyzer import (
    analyze_call
)

# --------------------------------
# Page Config
# --------------------------------

st.set_page_config(
    page_title="Enterprise AI Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Copilot")

st.markdown("""
### 🚀 Enterprise AI Copilot

**Features**
- 📊 SQL Analytics Agent
- 📄 Document Intelligence (RAG)
- 🎙️ Voice Conversation Analytics
- 🔀 LangGraph Workflow
- ⚡ Groq LLM
""")

st.markdown("""
<style>

button[data-baseweb="tab"] {
    font-size: 22px !important;
    font-weight: 700 !important;
    padding-top: 18px !important;
    padding-bottom: 18px !important;
    min-height: 70px !important;
}

button[data-baseweb="tab"] p {
    font-size: 22px !important;
}

</style>
""", unsafe_allow_html=True)

tab_sql, tab_docs, tab_voice = st.tabs(
    [
        "📊 SQL Analytics Agent",
        "📄 Document AI Agent",
        "🎙️ Voice AI Agent"
    ]
)

# --------------------------------
# Session State
# --------------------------------

initialize_chat()

if "document_loaded" not in st.session_state:
    st.session_state.document_loaded = False

if "document_name" not in st.session_state:
    st.session_state.document_name = None

if "is_indexing" not in st.session_state:
    st.session_state.is_indexing = False

if "voice_sample" not in st.session_state:
    st.session_state.voice_sample = None


# --------------------------------
# Sidebar
# --------------------------------

provider, uploaded_file = render_sidebar()


# --------------------------------
# Document Upload & Indexing
# --------------------------------

if uploaded_file:

    if st.session_state.document_name != uploaded_file.name:

        st.session_state.is_indexing = True

        with st.spinner(
            f"📚 Indexing {uploaded_file.name}..."
        ):

            progress = st.progress(0)

            os.makedirs(
                "data/uploads",
                exist_ok=True
            )

            progress.progress(20)

            file_path = os.path.join(
                "data/uploads",
                uploaded_file.name
            )

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            progress.progress(40)

            # Load document

            if uploaded_file.name.endswith(".pdf"):

                text = load_pdf(file_path)

            else:

                text = load_docx(file_path)

            progress.progress(60)

            # Chunk document

            chunks = chunk_text(text)

            progress.progress(80)

            # Store vectors

            store_chunks(chunks)

            progress.progress(100)

        st.session_state.document_loaded = True
        st.session_state.document_name = uploaded_file.name
        st.session_state.is_indexing = False

        st.success(
            f"✅ Indexed: {uploaded_file.name}"
        )

        st.rerun()


# --------------------------------
# Status
# --------------------------------

if st.session_state.is_indexing:

    st.warning(
        "📚 Document is being indexed. Please wait..."
    )

elif st.session_state.document_loaded:

    st.success(
        f"✅ {st.session_state.document_name} ready for querying"
    )


# --------------------------------
# Display Chat History
# --------------------------------

with tab_sql:

    st.subheader("📊 Sales Analytics Agent")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Database Columns",
            "4"
        )

    with col2:
        st.metric(
            "Sample Records",
            "1000+"
        )

    st.markdown("### 📋 Available Data")

    st.markdown("""
- **customer_name** → Customer Name
- **product_name** → Product Purchased
- **revenue** → Revenue Generated
- **sale_date** → Date of Sale
""")

    st.markdown("### 💡 Example Questions")

    col1, col2 = st.columns(2)

    with col1:

        st.code(
            "Show top customers by revenue"
        )

        st.code(
            "Show total revenue"
        )

    with col2:

        st.code(
            "Show revenue by product"
        )

        st.code(
            "Show monthly sales trend"
        )

    st.markdown("### 🗄️ Sample Database Preview")

    sample = run_query(
        "SELECT * FROM sales LIMIT 5"
    )

    st.dataframe(
        sample,
        width="stretch",
        hide_index=True
    )

    st.divider()

    # display_messages()

with tab_docs:

    st.subheader("📄 Document Intelligence")

    st.markdown("""
Chat with documents using Retrieval-Augmented Generation (RAG).
""")

    st.markdown("### 📚 Try Sample Documents")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "📄 Resume Sample",
            key="resume_sample"
        ):

            with st.spinner(
                "📚 Loading and indexing Resume Sample..."
            ):

                file_path = (
                    "data/sample_documents/resume_sample.pdf"
                )

                text = load_pdf(file_path)

                chunks = chunk_text(text)

                store_chunks(chunks)

                st.session_state.document_loaded = True

                st.session_state.document_name = (
                    "Resume Sample"
                )

            st.success(
                "✅ Resume Sample ready for querying"
            )
    with col2:

        if st.button(
            "📄 Employee Handbook",
            key="employee_handbook"
        ):

            with st.spinner(
                "📚 Loading and indexing Employee Handbook..."
            ):

                file_path = (
                    "data/sample_documents/employee_handbook.pdf"
                )

                text = load_pdf(file_path)

                chunks = chunk_text(text)

                store_chunks(chunks)

                st.session_state.document_loaded = True

                st.session_state.document_name = (
                    "Employee Handbook"
                )

            st.success(
                "✅ Employee Handbook ready for querying"
            )

    with col3:

        if st.button(
        "📄 Company Policy",
        key="company_policy"
        ):

            with st.spinner(
                "📚 Loading and indexing Company Policy..."
            ):

                file_path = (
                    "data/sample_documents/company_policy.pdf"
                )

                text = load_pdf(file_path)

                chunks = chunk_text(text)

                store_chunks(chunks)

                st.session_state.document_loaded = True

                st.session_state.document_name = (
                    "Company Policy"
                )

            st.success(
                "✅ Company Policy ready for querying"
            )

    st.markdown("""
Supported Formats:

- PDF
- DOCX
""")

    st.markdown("### 💡 Example Questions")

    st.code(
        "Summarize this document"
    )

    st.code(
        "What are the key takeaways?"
    )

    st.code(
        "List important skills from this resume"
    )

    st.code(
        "Create an executive summary"
    )

with tab_voice:

    st.subheader(
        "🎙️ Voice Conversation Analytics"
    )

    st.markdown("""
Analyze customer support calls, sales conversations,
meeting recordings, and interview discussions using AI.
""")

    st.markdown("### 🎧 Try Sample Calls")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "😡 Negative Support Call",
            key="negative_call"
        ):

            st.session_state.voice_sample = (
                "data/sample_calls/customer_support_negative.wav"
            )

    with col2:

        if st.button(
            "😊 Positive Support Call",
            key="positive_call"
        ):

            st.session_state.voice_sample = (
                "data/sample_calls/customer_support_positive.wav"
            )

    st.markdown("### 📤 Or Upload Your Own Recording")

    voice_file = st.file_uploader(
        "Upload Audio Recording",
        type=[
            "mp3",
            "wav",
            "m4a"
        ],
        key="voice_upload"
    )

    if voice_file or st.session_state.voice_sample:

        # --------------------
        # Decide Audio Source
        # --------------------

        if voice_file:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".wav"
            ) as tmp:

                tmp.write(
                    voice_file.getbuffer()
                )

                audio_path = tmp.name

            st.success(
                f"✅ Uploaded: {voice_file.name}"
            )

        else:

            audio_path = (
                st.session_state.voice_sample
            )

            st.success(
                f"✅ Loaded Sample Call: "
                f"{os.path.basename(audio_path)}"
            )

        # --------------------
        # Transcription
        # --------------------

        with st.spinner(
            "🎙️ Transcribing audio..."
        ):

            transcript = transcribe_audio(
                audio_path
            )

        st.markdown(
            "### 📝 Transcript"
        )

        st.text_area(
            "Generated Transcript",
            transcript,
            height=250
        )

        # --------------------
        # Analysis
        # --------------------

        with st.spinner(
            "📊 Analyzing conversation..."
        ):

            analysis = analyze_call(
                transcript
            )

        st.markdown(
            "### 📈 Call Analysis"
        )

        st.markdown(
            analysis
        )

    else:

        st.markdown("### 🚀 What You'll Get")

        col1, col2 = st.columns(2)

        with col1:

            st.code(
                "Call Summary"
            )

            st.code(
                "Customer Sentiment"
            )

            st.code(
                "Customer Intent"
            )

        with col2:

            st.code(
                "Action Items"
            )

            st.code(
                "Resolution Status"
            )

            st.code(
                "Key Discussion Points"
            )

        st.markdown("### 💡 Example Questions")

        st.code(
            "Analyze this customer support call"
        )

        st.code(
            "Summarize this sales conversation"
        )

        st.code(
            "What action items were discussed?"
        )

        st.code(
            "Was the customer satisfied?"
        )
        
st.divider()

if st.session_state.messages:

    st.divider()

    st.subheader("💬 AI Copilot Chat")

    display_messages()
# --------------------------------
# LLM
# --------------------------------

llm = LLMService()


# --------------------------------
# Prevent Queries During Indexing
# --------------------------------

if st.session_state.is_indexing:
    st.stop()


# --------------------------------
# Chat Input
# --------------------------------

user_input = st.chat_input(
    "Ask me anything...",
    disabled=st.session_state.is_indexing
)

# --------------------------------
# Handle User Query
# --------------------------------

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        try:

            result = graph.invoke(
                {
                    "question": user_input,
                    "document_loaded": st.session_state.document_loaded
                }
            )

            response = result["response"]

            st.markdown(response)

            if result.get("sql_result") is not None:

                with st.expander(
                    "Generated SQL",
                    expanded=False
                ):
                    st.code(
                        result["sql_query"],
                        language="sql"
                    )

                st.dataframe(
                    result["sql_result"],
                    width="stretch",
                    hide_index=True
                )

        except Exception as e:

            response = (
                f"❌ Error:\n\n{str(e)}"
            )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

