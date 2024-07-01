FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY calculate_metrics.py calculate_metrics.py

CMD ["python", "calculate_metrics.py"]
