FROM python:3-alpine

WORKDIR /usr/src/app

ENV DOCKER 1

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apk --no-cache add libpq

COPY app/ .
USER nobody
CMD gunicorn \
    --workers 2 \
    --threads 1 \
    --timeout 100 \
    --access-logfile '-' \
    --bind 0.0.0.0:8000 \
    mtls.wsgi
