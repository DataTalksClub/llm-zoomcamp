## Additional notes for those trying the streamlit/grafana out

1. the following packages maybe required when you run some of .py scripts

```
pip install psycopg2-binary
pip install python-dotenv
pip install pgcli
```


2) To download the phi3 model to the container
```
docker-compose up -d
docker-compose exec ollama ollama pull phi3
