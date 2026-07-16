# Pharma Risk Intelligence System

A Retrieval-Augmented Generation (RAG) application that allows users to upload pharmaceutical PDF documents and ask questions about their contents.

The system extracts text from PDFs, creates embeddings using Sentence Transformers, stores them in ChromaDB, retrieves relevant information, and uses Llama 3.3 (via Groq) to generate answers.

## Features

- Upload multiple PDF documents
- Automatic text extraction and chunking
- Semantic search using embeddings
- ChromaDB vector storage
- LLM-powered question answering
- Multi-document retrieval
- Conversation history
- Source chunk display for transparency

## Tech Stack

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- Groq API
- Llama 3.3 70B

## Project Structure

```text
Pharma-Risk-Intelligence-System

├── app.py
├── requirements.txt
├── README.md
├── data/
├── vectorstore/
├── .streamlit/
└── src/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── embeddings.py
    ├── vectorstore.py
    ├── retriever.py
    └── llm.py
```

## Setup

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a file:

```text
.streamlit/secrets.toml
```

Add your Groq API key:

```toml
GROQ_API_KEY = "your_api_key"
```

Run the application:

```bash
streamlit run app.py
```

## Usage

1. Upload one or more PDF documents.
2. Click **Process Documents**.
3. Ask questions about the uploaded documents.
4. View the generated answer and retrieved source chunks.

Example questions:

- What is Metformin used for?
- What precautions should elderly patients follow while taking Losartan?
- What are the side effects of Aspirin?
- Is Paracetamol safe during pregnancy?

## Future Improvements

- Source document citations
- Conversational memory
- Hybrid search
- Cloud deployment

## Author

Mahi Raj