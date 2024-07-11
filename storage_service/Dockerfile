FROM python:3.12.4

RUN mkdir "/storage_service"

COPY src/ /storage_service/src/
COPY src/alembic.ini /storage_service/src/
COPY poetry.lock /storage_service/
COPY pyproject.toml /storage_service/
COPY README.md /storage_service/
COPY start.sh /storage_service/

WORKDIR /storage_service

ENV POETRY_VIRTUALENVS_CREATE=false

RUN curl -sSL https://install.python-poetry.org | python3 - 
RUN $HOME/.local/bin/poetry install
RUN pip install alembic

CMD sh start.sh
