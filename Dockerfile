FROM python:3.12.5-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/poetry/.venv" \
    LC_ALL=C.UTF-8

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:/root/.local/bin:/root/.poetry/bin:$PATH"

WORKDIR $PYSETUP_PATH

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --user pipx \
    && python -m pipx ensurepath \
    && pipx ensurepath --global

RUN pipx install poetry==${POETRY_VERSION}

EXPOSE 8000

COPY config/docker/entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]


FROM base AS development
ENV ENV=development
WORKDIR /code
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --sync --with dev
COPY . /code/

FROM base AS production
ENV ENV=production
WORKDIR /code
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --sync --without dev
COPY . /code/
