FROM python:3.11-slim

WORKDIR /app

COPY ./4.2-monitoring-llms/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./4.2-monitoring-llms/. /app/.
COPY ./utils/. /app/utils/.

CMD ["python", "main.py"]
