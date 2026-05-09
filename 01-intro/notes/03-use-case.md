# The Use Case: Course FAQ

Throughout this workshop, our knowledge base is the
[DataTalks.Club FAQ](https://datatalks.club/faq) - a collection of
questions and answers from our Zoomcamp courses (machine learning,
data engineering, MLOps, LLM).

The dataset is available as JSON. Each entry looks like this:

```json
{
  "course": "machine-learning-zoomcamp",
  "course_name": "ML Zoomcamp",
  "section": "Module 1: Introduction",
  "question": "How do I install Python?",
  "answer": "Download it from python.org..."
}
```

We'll build a RAG system that can answer questions about these
courses by searching the FAQ and feeding the results to an LLM.
