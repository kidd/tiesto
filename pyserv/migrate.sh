PGPASSWORD="$PGPASSWORD" psql -h "db" -p 5432 testdb postgres -f ./migrate.sql
