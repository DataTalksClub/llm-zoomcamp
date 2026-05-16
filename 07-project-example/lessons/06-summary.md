# Summary and Closing Remarks

<a href="https://www.youtube.com/watch?v=TW9M5VE8vpo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/TW9M5VE8vpo">
</a>

Between the previous video and this one, the project was polished
further. Let's look at what changed and the final result.

## Post-recording improvements

Several improvements were made after recording:

- PostgreSQL logging was finished (there were timestamp issues with
  Docker clocks being out of sync with the host)
- Grafana dashboard provisioning was automated with an init script
  that creates the data source and loads the dashboard JSON
- The README was polished with a generated banner image, better
  formatting, grammar fixes, and clearer instructions
- Code readability improvements across all files

## Total cost

The entire project cost about $2 in OpenAI API calls:

- Dataset generation: ~$0.50
- Ground truth generation: ~$0.50
- RAG evaluation: ~$0.50
- Testing and debugging: ~$0.50

Using GPT-4o-mini keeps costs low. You could reduce costs
further by using a local model or a cheaper provider.

## Tips for your project

Keep these points in mind as you build your own project:

- Start simple: get a basic RAG flow working first, then add
  evaluation, monitoring, and containerization
- Use generated data if you don't have real data - it's good
  enough for a course project
- Polish your README: it's the first thing people see
- Use the course project criteria as a checklist

## The final project

Check out the completed project at
[alexeygrigorev/fitness-assistant](https://github.com/alexeygrigorev/fitness-assistant).

It includes:

- A fitness exercise dataset generated with GPT
- Search with minsearch
- RAG flow with OpenAI
- Retrieval and RAG evaluation
- Flask API
- Docker Compose with PostgreSQL and Grafana
- Automated Grafana provisioning
- A polished README

[← Monitoring and Containerization](05-monitoring.md) | [Chunking for Longer Texts →](07-chunking.md)
