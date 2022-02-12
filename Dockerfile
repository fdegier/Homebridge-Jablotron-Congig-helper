FROM python:3.9.7-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8080

ARG API_VERSION="dev"
ENV API_VERSION=$API_VERSION

CMD  ["uvicorn", "app:app", "--no-access-log", "--host", "0.0.0.0", "--port", "8080"]
