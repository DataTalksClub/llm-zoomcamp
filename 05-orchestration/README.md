# Data Preparation in RAG

## 1. Ingest

<a href="https://youtu.be/jTWFh8ocDDY">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

In this section, we cover the ingestion of documents from a single data source.

<a href="https://youtu.be/eg7xPhGWCcU">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

## 2. Chunk

<a href="https://youtu.be/aZkdusiBr10">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

Once data is ingested, we break it into manageable chunks.
This section explains the importance of chunking data and various techniques.


## 3. Tokenization

<a href="https://youtu.be/SpoepeljNGc">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

Tokenization is a crucial step in text processing and preparing the data for effective retrieval.


## 4. Embed

<a href="https://youtu.be/BmlDmGMnrEA">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

Embedding data translates text into numerical vectors that can be processed by models.

* Notebook: [demo_embed.ipynb](demo_embed.ipynb)


## 5. Export

<a href="https://youtu.be/nhdG09vZqtc">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

After processing, data needs to be exported for storage so that it can be retrieved for better contextualization of user queries.


## 6. Test Vector Search Query

<a href="https://youtu.be/BDgzv5nDt5g">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

<a href="https://youtu.be/2A7h4dWV8xA">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

After exporting the chunks and embeddings, we can test the search query to retrieve relevant documents on sample queries.

* Notebook: [demo_test_query.ipynb](demo_test_query.ipynb)


## 7. Trigger Daily Runs

<a href="https://youtu.be/7JyWw1F50CE">
  <img src="https://github.com/user-attachments/assets/9cc07237-add9-462e-9272-6e52eb918c9a">
</a>

Automation is key to maintaining and updating your system.
This section demonstrates how to schedule and trigger daily runs for your data pipelines, ensuring up-to-date and consistent data processing.


# Notes

- All videos: https://www.youtube.com/playlist?list=PL_ItKjYd0Dsg86be-K5GqMbA4VLBJT5Pc
