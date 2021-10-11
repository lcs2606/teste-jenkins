FROM python:3.9.7-alpine3.14

WORKDIR /app
COPY app.py .
ENTRYPOINT [ "python3", "app.py" ]
