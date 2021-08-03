FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache \
pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
COPY . .
CMD gunicorn --bind 0.0.0.0:$PORT app:app