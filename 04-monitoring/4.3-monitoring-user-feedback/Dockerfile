FROM python:3.11-slim

WORKDIR /app

COPY ./4.3-monitoring-user-feedback/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./4.3-monitoring-user-feedback/. .
COPY ./utils/. /app/utils/.

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
