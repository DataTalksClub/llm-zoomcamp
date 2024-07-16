FROM python:3.11-slim

WORKDIR /app

COPY ./04-monitoring/4.2-monitoring-llms/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./04-monitoring/4.2-monitoring-llms/. /app/.
COPY ./04-monitoring/utils/. /app/utils/.

COPY ./03-vector-search/eval/documents-with-ids.json documents-with-ids.json

CMD ["python", "main.py"]
