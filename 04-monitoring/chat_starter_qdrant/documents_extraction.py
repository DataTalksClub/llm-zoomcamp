import uuid

import requests
from config import DOCS_URL, QDRANT_HOST, COLLECTION_NAME, EMBEDDING_DIMENSIONALITY, MODEL_HANDLE
from qdrant_client import models, QdrantClient

class QdrantVectorStore:
    def __init__(self, host: str):
        self.client = QdrantClient(url=host)

    def create_collection(self, collection_name: str, embedding_dimensionality: int):
        if not self.client.collection_exists(collection_name=collection_name):
            self.client.create_collection(collection_name=collection_name,
                                        vectors_config=models.VectorParams(
                                            size=embedding_dimensionality,
                                            distance=models.Distance.COSINE
                                        )
                                        )
        else:
            print(f"Collection {collection_name} already exists.")

    def create_collection_sparse(self, collection_name: str):
        if not self.client.collection_exists(collection_name=collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                sparse_vectors_config={
                    "bm25": models.SparseVectorParams(
                        modifier=models.Modifier.IDF
                    )
                }
            )
        else:
            print(f"Collection {collection_name} already exists.")
            
    def create_collection_hybrid(self, collection_name: str, embedding_dimensionality: int):
        if not self.client.collection_exists(collection_name=collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config={
                    "jina-small": models.VectorParams(
                        size=embedding_dimensionality,
                        distance=models.Distance.COSINE
                    )
                },
                sparse_vectors_config={
                    "bm25": models.SparseVectorParams(
                        modifier=models.Modifier.IDF
                    )
                }
            )
        else:
            print(f"Collection {collection_name} already exists.")


def fetch_docs(url: str):
    response = requests.get(url)
    return response.json()


def upsert_documents(client, collection_name: str, model_handle_dense: str, model_handle_sparse: str, documents: list):
    client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(
                id=uuid.uuid4().hex,
                vector={
                    "jina-small": models.Document(
                        text=doc["text"],
                        model=model_handle_dense
                        ),
                    "bm25": models.Document(
                        text=doc["text"],
                        model=model_handle_sparse
                        )
                    },
                payload={
                    "text": doc["text"],
                    "section": doc["section"],
                    "course": course['course']
                }
            )
        for course in documents for doc in course["documents"]
        ]
    )
    

if __name__ == "__main__":
    # Fetch documents
    documents_raw = fetch_docs(DOCS_URL)

    # Initialize Qdrant client
    qv = QdrantVectorStore(host=QDRANT_HOST)

    # Create collection
    COLLECTION_NAME = "zoomcamo-rag-sparse-dense"
    qv.create_collection_hybrid(collection_name=COLLECTION_NAME, embedding_dimensionality=EMBEDDING_DIMENSIONALITY)

    # Upsert documents
    upsert_documents(client=qv.client,
                     collection_name=COLLECTION_NAME,
                     documents=documents_raw,
                     model_handle_sparse="Qdrant/bm25",
                     model_handle_dense="jinaai/jina-embeddings-v2-small-en"
                     )