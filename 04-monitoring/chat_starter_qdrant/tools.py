import json
from qdrant_client import QdrantClient, models
from openai import OpenAI
import os
from config import QDRANT_HOST, COLLECTION_NAME
from tracing import tracer


class Tools:

    def __init__(self):
        self.tools = {}
        self.functions = {}

    def add_tool(self, func, description):
        """Add a tool with its function and description."""
        self.tools[func.__name__] = description
        self.functions[func.__name__] = func

    def get_tools(self):
        """Get the dictionary of tools."""
        return list(self.tools.values())
    
    def function_call(self, tool_name):
        """Call a tool function by its name."""
        function_name = tool_name.name
        arguments = json.loads(tool_name.arguments)
        if function_name in self.functions:
            func = self.functions[function_name]
            result =  func(**arguments)
            return {
                "type": "function_call_result",
                "call_id": tool_name.call_id,
                "output": json.dumps(result, indent=2)
            }
        else:
            raise ValueError(f"Tool '{function_name}' not found.")
        


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

class OpenAIClient:
    def __init__(self, api_key, model="gpt-4.1-nano"):
        """
        Initializes the OpenAI client with the provided API key.
        
        Args:
            api_key (str): OpenAI API key.
            model (str, optional): The model to use for chat completions. Defaults to "gpt-4.1-nano".
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, query: str):
        """
        Sends a chat request to the OpenAI API.
        
        Args:
            query (str): The query to send to the OpenAI API.

        Returns:
            Response from the OpenAI API.
        """
        response =  self.client.chat.completions.create(model=self.model,
                                                        messages=[{"role": "user", "content": query}]
                                                        )

        return response.choices[0].message.content
    
    def chat_stream(self, messages):
        """
        Sends a streaming chat request to the OpenAI API.
        
        Args:
            messages (list): List of messages to send to the OpenAI API.

        """
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in messages],
            stream=True
        )
        return stream


def build_context(result):
    """
    Builds a context string from the provided documents.
    
    Args:
        documents (list): List of documents to build the context from.
        
    Returns:
        str: A formatted string containing the context from the documents.
    """
    context = ""
    for point in result:
        if isinstance(point, tuple):
            for doc in point[1]:
                context += f"Section: {doc.payload['section']}\nanswer: {doc.payload['text']}\n\n"
                course = doc.payload['course']
        else:
            doc = point.payload
            context += f"Section: {doc['section']}\nanswer: {doc['text']}\n\n"
            course = doc['course']
    context = f"Course: {course}" + "\n\n" + context
    return context

class SearchTool:
    
    def __init__(self, client: QdrantClient, collection_name: str):
        self.client = client
        self.collection_name = collection_name

    search_tool = {
        "type": "function",
        "name": "search",
        "description": "Search the FAQ database",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query text to look up in the course FAQ."
                }
            },
            "required": ["query"],
            "additionalProperties": False
        }
    }

    def search_hybrid(self, query: str, limit: int=1, filter_key: str=None, filter_value: str="mlops-zoomcamp") -> list[models.ScoredPoint]:
        
        with tracer.start_as_current_span("retrieve") as span:
            try:
                results = self.client.query_points(
                collection_name=self.collection_name,
                prefetch=[
                    models.Prefetch(
                        query=models.Document(
                            text=query,
                            model="jinaai/jina-embeddings-v2-small-en"
                        ),
                        using='jina-small',
                        limit=(limit*5),
                        filter=models.Filter(
                            must=[
                                models.FieldCondition(
                                    key=filter_key,
                                    match=models.MatchValue(value=filter_value)
                                )
                            ]
                        )
                    ),
                    models.Prefetch(
                        query=models.Document(
                            text=query,
                            model="Qdrant/bm25"
                        ),
                        using="bm25",
                        limit=(limit*5),
                        filter=models.Filter(
                            must=[
                                models.FieldCondition(
                                    key=filter_key,
                                    match=models.MatchValue(value=filter_value)
                                )
                            ]
                        )
                    )
                ],
                query=models.FusionQuery(
                    fusion=models.Fusion.RRF
                ),
                with_payload=True,
                limit=limit
                )
                span.set_attribute("openinference.span.kind", "RETRIEVER")
                span.set_attribute("input.value", query)
                span.set_attribute("retrieval.top_k", limit)
                span.set_attribute("retrieval.filter", json.dumps({f'{filter_key}': f'{filter_value}'}))


                for i, doc in enumerate(results.points):
                    prefix = f"retrieval.document.{i}.document"
                    doc_id = doc.id if isinstance(doc, object) else i
                    span.set_attribute(f"{prefix}.id", str(doc_id))

                    if isinstance(doc, object) and doc.score:
                        span.set_attribute(f"{prefix}.score", float(doc.score))

                    if isinstance(doc, object) and doc.payload:
                        span.set_attribute(f"{prefix}.payload", json.dumps(doc.payload["text"][:100]))
                    else:
                        span.set_attribute(f"{prefix}.payload", str(doc)[:500])
                    
                    span.add_event(
                        name=f"retrieved_document_{i}_{doc_id if doc_id else i}",
                        attributes={
                            "document.index": i,
                            "document.id": doc_id if doc_id else str(i),
                            "document.score": doc.score if isinstance(doc, object) and doc.score else None,
                            "document.payload": json.dumps(doc.payload["text"][:100]) if isinstance(doc, object) and doc.payload else str(doc)[:500]
                        }
                    )
                span.set_attribute("retrieval.documents.count", int(len(results.points)))
                return results.points
            except Exception as e:
                span.record_exception(e)
                span.set_status("ERROR")
                raise e

if __name__ == "__main__":

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    qv = QdrantVectorStore(host=QDRANT_HOST)

    MODEL = "gpt-4.1-nano"
    prompt_template = """
    You are a course assistant, and your goal is to answer questions of students, where QUESTION is provided below and CONTEXT is provided most of the times. 
    Rules:
    * Answer the QUESTION based on the CONTEXT.
    * Use only the facts from the CONTEXT.
    * If CONTEXT is empty, please let the student know, the information about their query is not there, however you found the following information on the web, by searching the web

    QUESTION: {question}

    CONTEXT: {context}
    """.strip()

    query = "When can I start the course?"
    sv = SearchTool(client=qv.client,
                    collection_name=COLLECTION_NAME)
    results = sv.search_hybrid(query=query,
                               limit=1,
                               filter_key="course",
                               filter_value="mlops-zoomcamp")
    
    print("Search Results")
    print(results)