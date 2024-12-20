# Dockerfile which can be used for deploying the bot as a Docker container.

FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD ["python", "-O", "src/main.py"]
