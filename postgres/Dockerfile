FROM postgres:16.3-alpine3.20

RUN mkdir "/postgres"
COPY postgresql.conf /postgres
COPY pg_hba.conf /postgres
COPY update_config.sh /docker-entrypoint-initdb.d/_updateConfig.sh


WORKDIR /


