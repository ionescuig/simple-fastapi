# ------------ Install dependencies ------------
FROM python:3.12-slim AS base

WORKDIR /app
ARG POETRY_VERSION=1.8.3
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN pip install --no-cache-dir poetry==${POETRY_VERSION} uvicorn[standard]


# ------------ Dev environment ------------
FROM base AS dev
COPY pyproject.toml poetry.lock ${WORKDIR}
RUN poetry install --no-ansi
COPY ./src ${WORKDIR}/app/
COPY entrypoint ${WORKDIR}/entrypoint
ENTRYPOINT ["/entrypoint"]

# ------------ Prod environment ------------
FROM base AS prod
COPY pyproject.toml poetry.lock ${APP_HOME}
RUN poetry install --no-ansi --without dev
COPY ./src ${WORKDIR}/app/
COPY entrypoint ${WORKDIR}/entrypoint
ENTRYPOINT ["/entrypoint"]
