FROM python:3.11-slim

WORKDIR /app

COPY ./4.2-monitoring-llms/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./4.2-monitoring-llms/. /app/.
COPY ./utils/. /app/utils/.
COPY ../03-vector-search/eval/documents-with-ids.json documents-with-ids.json
COPY ../03-vector-search/eval/ground-truth-data.csv ground-truth-data.csv

CMD ["python", "main.py"]
