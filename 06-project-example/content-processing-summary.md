# Content Processing Cases and Steps

## Case: Multiple Articles

- Assign each article a document id
- Chunk the articles
- Assign each chunk a unique chunk id (could be doc_id + chunk_number)
- Evaluate retrieval: separate hitrate for both doc_id and chunk_id
- Evaluate RAG: LLM as a Judge
- Tuning chunk size: use metrics from Evaluate RAG

Example JSON structure for a chunk:
```json
{
  "doc_id": "ashdiasdh",
  "chunk_id": "ashdiasdh_1",
  "text": "actual text"
}
```

## Case: Single Article / Transcript / Etc.

Example: the user provides YouTubeID, you initialize the system and now you can talk to it
  
- Chunk it
- Evaluation as for multiple articles


## Case: Book or Very Long Form Content

- Experiment with it
- Each chapter / section can be a separate document
- Use LLM as a Judge to see which approach works best

## Case: Images

- Describe the images using gpt-4o-mini
- [CLIP](https://openai.com/index/clip/)
- Each image is a separate document

## Case: Slides

- Same as with images + multiple articles
- "Chunking": slide deck = document, slide = chunk
