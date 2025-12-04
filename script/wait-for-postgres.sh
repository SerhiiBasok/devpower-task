#!/bin/sh
set -e

host="$1"
shift
cmd="$@"

until pg_isready -h "$host" -p 5432; do
  echo "Waiting for postgres at $host:5432..."
  sleep 1
done

echo "Postgres is ready!"
exec $cmd
