import requests
from minsearch import Index


def init_index():
    docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
    docs_response = requests.get(docs_url)
    documents_raw = docs_response.json()

    documents = []

    for course in documents_raw:
        course_name = course['course']

        for doc in course['documents']:
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

        results = self.index.search(
            query=query,
            filter_dict={'course': 'data-engineering-zoomcamp'},
            boost_dict=boost,
            num_results=5,
            output_ids=True
        )

        return results

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