import tempfile
import streamlit as st
from src.llm import generate_answer

from src.pdf_loader import extract_text
from src.text_splitter import create_chunks
from src.embeddings import generate_embeddings
from src.vectorstore import store_embeddings
from src.retriever import search


# ==========================
# Streamlit UI
# ==========================

st.set_page_config(
    page_title="Pharma Risk Intelligence System",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Pharma Risk Intelligence System")
st.write(
    "Upload one or more PDFs and ask questions about them."
)

# --------------------------
# Session State
# --------------------------

if "processed" not in st.session_state:
    st.session_state.processed = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# --------------------------
# Upload PDFs
# --------------------------

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# --------------------------
# Process Documents
# --------------------------

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} PDF(s) uploaded successfully!"
    )

    if st.button("Process Documents"):

        with st.spinner(
            "Extracting text and creating embeddings..."
        ):

            all_chunks = []

            for uploaded_file in uploaded_files:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_file:

                    temp_file.write(
                        uploaded_file.read()
                    )

                    pdf_path = temp_file.name

                text = extract_text(
                    pdf_path
                )

                chunks = create_chunks(
                    text,
                    chunk_size=1000,
                    overlap=200
                )

                all_chunks.extend(
                    chunks
                )

            embeddings = generate_embeddings(
                all_chunks
            )

            store_embeddings(
                all_chunks,
                embeddings
            )

            st.session_state.processed = True

        st.success(
            f"Indexed {len(all_chunks)} chunks successfully!"
        )

# --------------------------
# Ask Questions
# --------------------------

if st.session_state.processed:

    query = st.text_input(
        "Ask a question"
    )

    if st.button("Ask"):

        if query:

            results, scores = search(
            query=query,
            top_k=7)

            context = "\n\n".join(results)

            answer = generate_answer(
            query=query,
            context=context)

            st.session_state.chat_history.append(
                {
                    "question": query,
                    "answer": answer,
                    "sources": results,
                    "scores": scores
                }
            )

# --------------------------
# Chat History
# --------------------------

if st.session_state.chat_history:

    st.subheader("Conversation")

    for idx, item in enumerate(
            st.session_state.chat_history,
            start=1):

        st.markdown(
            f"### Question {idx}"
        )

        st.markdown(
            f"**Q:** {item['question']}"
        )

        st.markdown(
            f"**A:** {item['answer']}"
        )

        with st.expander(
            "View Retrieved Chunks"
        ):

            for i, chunk in enumerate(
                    item["sources"]):

                st.markdown(
                    f"**Chunk {i+1}**"
                )

                st.write(chunk)

                if item["scores"]:

                    st.caption(
                        f"Distance Score: {item['scores'][i]}"
                    )

        st.markdown("---")