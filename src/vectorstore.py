import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./vectorstore"
)

collection = client.get_or_create_collection(
    name="medical_docs"
)


def store_embeddings(chunks, embeddings):

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print(
        f"Stored {len(chunks)} chunks successfully"
    )