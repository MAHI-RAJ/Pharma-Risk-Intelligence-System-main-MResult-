from src.vectorstore import collection
from src.embeddings import model


def search(query, top_k=3):

    query_embedding = model.encode(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    return documents, distances