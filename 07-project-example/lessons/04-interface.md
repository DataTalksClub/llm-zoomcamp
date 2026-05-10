# Interface and Ingestion Pipeline

<a href="https://www.youtube.com/watch?v=vMHve2EyA5M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/vMHve2EyA5M">
</a>

So far we've been working in notebooks. Now we turn the notebook
into a proper application with an ingestion pipeline and a web API.


## From notebook to scripts

Convert the notebook to Python scripts:

```bash
jupyter nbconvert --to=script rag_test.ipynb
```

Then split the code into a package structure:

```
fitness_assistant/
    __init__.py
    rag.py          # RAG flow
    search.py       # Search index
app.py              # Flask API
ingest.py           # Load data into index
```

The ingestion script loads the dataset and builds the search index:

```python
from fitness_assistant.search import Index
import json

def load_index():
    with open('data/exercises.json') as f:
        documents = json.load(f)

    index = Index(
        text_fields=["exercise", "instructions", "muscle_group"],
        keyword_fields=["id"]
    )
    index.fit(documents)
    return index
```

Since we're using minsearch (in-memory), the ingestion happens when
the app starts. If you use a real database like Elasticsearch, the
ingestion would be a separate step.


## Flask API

Create a simple API endpoint:

```python
from flask import Flask, request, jsonify
from fitness_assistant.rag import rag

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    answer = rag(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Install Flask:

```bash
uv add flask
```

Test it:

```bash
uv run python app.py
```

Then send a request:

```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What exercises target the chest?"}'
```


## Improving the README

Update the README with instructions for:

- Installing dependencies (`uv sync`)
- Running the ingestion pipeline
- Starting the API server
- Example API calls

A good README makes it easy for anyone to run your project.


[<< Previous: Evaluating RAG](03-evaluating-rag)
|
[Next: Monitoring and Containerization >>](05-monitoring)
