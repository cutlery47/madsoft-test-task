FROM python:3.12.4

RUN mkdir "/public_service"

COPY src/ /public_service/src/
COPY poetry.lock /public_service/
COPY pyproject.toml /public_service/
COPY README.md /public_service/
COPY start.sh /public_service/

WORKDIR /public_service

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN $HOME/.local/bin/poetry install

CMD sh start.sh