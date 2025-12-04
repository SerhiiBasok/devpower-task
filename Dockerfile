FROM python:3.12-slim

LABEL maintainer="sergeybsk19@gmail.com"

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi


COPY . .

COPY script/wait-for-postgres.sh /app/script/wait-for-postgres.sh
RUN chmod +x /app/script/wait-for-postgres.sh
