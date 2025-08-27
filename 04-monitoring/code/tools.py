import json
import os
import time
import requests 
from minsearch import Index  
from tracing import tracer

def shorten(text, max_length=50):
    if len(text) <= max_length:
        return text

    return text[:max_length - 3] + "..."

class Tools:

    def __init__(self):
        self.tools = {}
        self.functions = {}

    def add_tool(self, function, description):
        self.tools[function.__name__] = description
        self.functions[function.__name__] = function
    
    def get_tools(self):
        return list(self.tools.values())

    def function_call(self, tool_call_response):
        function_name = tool_call_response.name
        arguments = json.loads(tool_call_response.arguments)

        f = self.functions[function_name]
        result = f(**arguments)

        return {
            "type": "function_call_output",
            "call_id": tool_call_response.call_id,
            "output": json.dumps(result, indent=2),
        }

def init_index():
    docs_url = os.getenv('DOCS_URL', 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json')
    documents_raw = None
    http_status = None
    last_error = None
    for attempt in range(3):
        try:
            resp = requests.get(docs_url, timeout=10)
            http_status = int(resp.status_code)
            if 200 <= http_status < 300:
                documents_raw = resp.json()
                break
            last_error = RuntimeError(f"HTTP {http_status}")
        except Exception as e: 
            last_error = e
        time.sleep(0.5 * (2 ** attempt))

    if documents_raw is None:
        local_path = os.path.join(os.path.dirname(__file__), 'documents.json')
        try:
            if os.path.exists(local_path):
                with open(local_path, 'r') as f:
                    documents_raw = json.load(f)
        except Exception as e:
            last_error = e

    if documents_raw is None:
        documents_raw = [
            {
                "course": "data-engineering-zoomcamp",
                "documents": [
                    {
                        "question": "What is the Data Engineering Zoomcamp?",
                        "section": "introduction",
                        "text": "A community course on data engineering fundamentals and projects.",
                    }
                ],
            }
        ]
    
    documents = []
    for course in documents_raw:
        course_name = course.get('course', 'unknown') if isinstance(course, dict) else 'unknown'
        documents_list = course.get('documents', []) if isinstance(course, dict) else []
        for doc in documents_list or []:
            if isinstance(doc, dict):
                doc['course'] = course_name
                documents.append(doc)

    index = Index(
        text_fields=["question", "text", "section"],
        keyword_fields=["course"]
    )

    index.fit(documents)
    return index


class SearchTool:
    def __init__(self, index):
        self.index = index

    def search(self, query):
        boost = {'question': 3.0, 'section': 0.5}

        with tracer.start_as_current_span("retrieve") as span:
            try:
                results = self.index.search(
                    query=query,
                    filter_dict={'course': 'data-engineering-zoomcamp'},
                    boost_dict=boost,
                    num_results=5,
                    output_ids=True
                )

                # OpenInference attributes for Retriever spans
                # Ref: https://arize.com/docs/phoenix/learn/tracing/what-are-traces#retriever
                span.set_attribute("openinference.span.kind", "RETRIEVER")
                span.set_attribute("input.value", query)
                span.set_attribute("retrieval.top_k", 5)
                span.set_attribute("retrieval.filter", json.dumps({'course': 'data-engineering-zoomcamp'}))
                span.set_attribute("retrieval.boost", json.dumps(boost))

                for i, doc in enumerate(results):
                    prefix = f"retrieval.documents.{i}.document"
                    doc_id = doc.get("id", i) if isinstance(doc, dict) else i
                    span.set_attribute(f"{prefix}.id", str(doc_id))

                    if isinstance(doc, dict) and "score" in doc:
                        try:
                            score = doc.get("score")
                            if score is not None:
                                span.set_attribute(f"{prefix}.score", float(score))
                        except Exception:
                            pass

                    content_value = ""
                    if isinstance(doc, dict):
                        content_value = doc.get("text") or doc.get("question") or doc.get("section") or str(doc)
                    else:
                        content_value = str(doc)
                    span.set_attribute(f"{prefix}.content", shorten(str(content_value), 500))

                    if isinstance(doc, dict):
                        metadata = {k: v for k, v in doc.items() if k not in ("id", "score", "text", "question", "section")}
                        if metadata:
                            try:
                                span.set_attribute(f"{prefix}.metadata", json.dumps(metadata))
                            except Exception:
                                span.set_attribute(f"{prefix}.metadata", shorten(str(metadata), 500))

                span.set_attribute("retrieval.documents.count", int(len(results)))
                return results
            except Exception as e:
                try:
                    span.record_exception(e)
                finally:
                    raise

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


