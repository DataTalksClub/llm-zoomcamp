Response Time Panel:

```sql
SELECT
  timestamp AS time,
  response_time
FROM conversations
ORDER BY timestamp
```

Relevance Distribution Panel:


```sql
SELECT
  relevance,
  COUNT(*) as count
FROM conversations
GROUP BY relevance
```

Model Usage Panel:

```sql
SELECT
  model_used,
  COUNT(*) as count
FROM conversations
GROUP BY model_used
```


Token Usage Panel:

```sql
SELECT
  timestamp AS time,
  total_tokens
FROM conversations
ORDER BY timestamp
```

OpenAI Cost Panel:

```sql
SELECT
  timestamp AS time,
  openai_cost
FROM conversations
WHERE openai_cost > 0
ORDER BY timestamp
```

Recent Conversations Panel:

```sql
SELECT
  timestamp AS time,
  question,
  answer,
  relevance
FROM conversations
ORDER BY timestamp DESC
LIMIT 5
```

Feedback Statistics Panel:

```sql
SELECT
  SUM(CASE WHEN feedback > 0 THEN 1 ELSE 0 END) as thumbs_up,
  SUM(CASE WHEN feedback < 0 THEN 1 ELSE 0 END) as thumbs_down
FROM feedback
```
