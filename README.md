# Steps

## Create env-file for database

Execute `cp db/.env.skelton db/.env`.

### Fill this file

E.g.

```
PGHOST=0.0.0.0
PGPORT=5432
PGDATABASE=idp
PGUSER=postgres
PGPASSWORD=postgrespassword
POSTGRES_DB=idp
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgrespassword
```

## Create [the connection service file](https://www.postgresql.org/docs/current/libpq-pgservice.html)

Execute `cp .pg_service.conf.skelton .pg_service.conf`.

### Fill this file

[Environment Variables Reference](https://www.postgresql.org/docs/current/libpq-envars.html)

E.g.

```
[db]
host=db
port=5432
dbname=idp
user=postgres
password=postgrespassword
```

## Create [the password file](https://www.postgresql.org/docs/current/libpq-pgpass.html)

Execute `cp .pgpass.skeleton .pgpass`.

### Fill this file

E.g.

```
db:5432:idp:postgres:postgrespassword
```
