FROM postgres:14.5-bullseye

COPY ./init.sql /docker-entrypoint-initdb.d/init.sql

ENV POSTGRES_USER some-postgres
ENV POSTGRES_PASSWORD mysecretpassword

EXPOSE 5432
