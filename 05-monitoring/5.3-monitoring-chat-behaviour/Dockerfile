FROM python:3.11-slim

WORKDIR /app

COPY ./5.3-monitoring-chat-behaviour/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./5.3-monitoring-chat-behaviour/. .
COPY ./utils/. /app/utils/.

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
