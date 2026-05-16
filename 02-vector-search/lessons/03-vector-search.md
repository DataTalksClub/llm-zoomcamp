# Embedding Our Dataset

TODO rename it to vector search. I already updated the file name

In the previous lesson, we saw how embeddings work with simple examples.

Now let's embed our entire FAQ dataset and see vector search in action.


## Loading the data

In the previous module, we created a helper script for downloading the 
data. You can see it here:  TODO: add the link to the file 

If you don't have it from the previous lesson, let's download it:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/code/ingest.py
```

Now we can use it:

```python
from ingest import load_faq_data

documents = load_faq_data()
```


## Generating embeddings

For vector search, we want to embed a combination of the question and
the answer. This way, when a user asks a question, we can match it
against both the questions and answers in our index:

```python
texts = []

for doc in documents:
    text = doc['question'] + ' ' + doc['answer']
    texts.append(text)
```

Now generate the embeddings. We'll do it in batches.

First we'll import `tqdm` - we'll need it to see the progress. 

```python
from tqdm.auto import tqdm
```

Now let's chunk the dataset into batches of 50 and encode the 
vectors:

```python
batch_size = 50
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch)
    vectors.extend(batch_vectors)

len(vectors)
```

Now we have 1208 vectors.

Let's turn them into a 2-dimentional array (matrix) where

- rows are documents (vectors)
- columns are dimenstions of the vectors

```python
import numpy as np
X = np.array(vectors)
```

The shape of this matrix `X` is (1208, 384) - number of documents vs number of dimensions.

TODO: split the file here. first we embed the dataset and then we do vector search


## Vector search

Now let's see how vector search works under the hood.

We have a matrix `X` with all document embeddings.

When a query comes in, we embed it:

```python
query = 'Can I still join the course after the start date?'
v_query = model.encode(query)
```

Next, we compute the dot product against all documents:

```python
scores = X.dot(v_query)
```

This is matrix-vector multiplication, and it's typically very very fast. Each element `i` of the `scores` vector is the cosine similarity between the document `i` (on row `i`) and `v_query`. 

The highest score is the most similar document:

```python
idx = np.argmax(scores)
idx, scores[idx]
```

This returns a document 553 with score 0.76.

Note: this may change for you because or dataset is evolving over time.

Let's see which document is it: 

```python
documents[idx]
```

We see:

```python
{'id': '3f1424af17',
 'course': 'data-engineering-zoomcamp',
 'section': 'General Course-Related Questions',
 'question': 'Course: Can I still join the course after the start date?',
 'answer': "Yes, even if you don't register, you're still eligible..."}
```

We can also look at the top 5 results:

```python
top5 = np.argsort(scores)[-5:]
```

We get the last 5 results (sorting it from lowest to highest in numpy).
This returns an array with 5 indicies: 

```python
array([558, 472,  29, 955, 553])
```

Next, we need to reverse them: 

```python
top5 = top5[::-1]
top5
```

Now we can see the top 5 scores: 

```python
scores[top5]
```

Let's see the actual documents:

```python
for idx in top5:
    print(scores[idx])
    print(documents[idx])
    print()
```

This is vector search in its simplest form: embed the query, compute
dot products with all documents, return the one with the highest score.

Doing this manually with numpy works fine for small datasets. For
larger ones, you'd want a search library that handles filtering and ranking.
We'll use special libraries for that.

[← Embeddings](02-embeddings.md) | [Vector Search with minsearch →](04-minsearch-vector.md)
