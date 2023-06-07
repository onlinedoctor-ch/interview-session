psql $(echo $DATABASE_URL | sed 's/+psycopg2//')
