FROM postgres:14.5-bullseye

COPY ./init.sql /docker-entrypoint-initdb.d/init.sql

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password

EXPOSE 5432
