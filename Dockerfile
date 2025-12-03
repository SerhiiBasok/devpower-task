FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
COPY app /app/app
COPY scripts /app/scripts
COPY commands/wait-for-postgres.sh /app/

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

RUN chmod +x /app/commands/wait-for-postgres.sh

CMD ["bash"]
