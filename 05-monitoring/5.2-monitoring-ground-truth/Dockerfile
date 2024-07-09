FROM python:3.11-slim

WORKDIR /app

COPY ./5.2-monitoring-ground-truth/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./5.2-monitoring-ground-truth/. /app/.
COPY ./utils/. /app/utils/.

CMD ["python", "metrics_computation.py"]
