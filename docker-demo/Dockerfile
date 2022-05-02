FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY docker_demo docker_demo

CMD ["gunicorn", "docker_demo.app:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:80"]
