from src.pdf_loader import extract_text
from src.text_splitter import create_chunks
from src.embeddings import generate_embeddings
from src.vectorstore import store_embeddings
from src.retriever import search

def run_pipeline(pdf_path):

    text = extract_text(pdf_path)

    chunks = create_chunks(text)

    embeddings = generate_embeddings(chunks)

    store_embeddings(
        chunks,
        embeddings
    )

    return True