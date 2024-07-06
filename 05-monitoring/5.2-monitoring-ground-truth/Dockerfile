FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY metrics_computation.py metrics_computation.py

CMD ["python", "metrics_computation.py"]
