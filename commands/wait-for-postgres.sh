set -e

host=$(echo "$DATABASE_URL" | sed -E 's#.*@([^:/]+).*#\1#' || echo "postgres")
port=5432

echo "Waiting for Postgres at $host:$port..."
until pg_isready -h "$host" -p "$port" >/dev/null 2>&1; do
  sleep 1
done
echo "Postgres is ready"
