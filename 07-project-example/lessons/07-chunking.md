# Chunking for Longer Texts

<a href="https://www.youtube.com/watch?v=tyBRP_WewXA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/tyBRP_WewXA">
</a>

Our FAQ data is well-structured: each document is a question-answer
pair. But what if your data is articles, transcripts, or slide
decks? You need to chunk it into pieces that are the right size
for embedding and retrieval.

## Multiple articles

If you have multiple articles (blog posts, wiki pages, etc.

):

1. Assign each article a document ID
2. Split each article into chunks
3. Give each chunk a unique chunk ID (e.g., `doc_id_1`, `doc_id_2`)
4. Evaluate retrieval with separate Hit Rate for both document ID
   and chunk ID
5. Tune chunk size using RAG evaluation metrics

```json
{
  "doc_id": "abc123",
  "chunk_id": "abc123_1",
  "text": "first paragraph of the article..."
}
```

## Single article or transcript

If you have one long piece of content (a YouTube transcript, a
PDF, etc.

):

1. Split it into chunks
2. Evaluate the same way as multiple articles
3. You can use `youtube-transcript-api` to get transcripts
   programmatically

## Book or very long content

For books and other long-form content, apply this strategy:

1. Treat each chapter or section as a separate document
2. Experiment with different chunking strategies
3. Use LLM-as-a-Judge to compare approaches

## Images and slides

Visual content can be processed as follows:

1. Describe images using an LLM like GPT-4o-mini
2. Each image is a separate document
3. For slide decks: deck = document, slide = chunk
4. You can also use CLIP embeddings for direct image search

## Smart chunking with LLMs

Instead of splitting by character count or paragraph breaks, you
can use an LLM to find logical boundaries:

1. Give the LLM the full text and ask it to split into logical
   blocks
2. Then ask it to name each block
3. Each block becomes a chunk you can index and search

This approach, sometimes called "semantic chunking" or "logical
chunking," often produces better chunks than fixed-size splitting
because the chunks map to meaningful topics.

You can see a detailed summary of content processing approaches
in [content-processing-summary.md](../content-processing-summary.md).

[← Summary and Closing Remarks](06-summary.md) | [Back to module →](../)
