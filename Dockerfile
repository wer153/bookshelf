FROM python:3.11-slim-bookworm
WORKDIR /code
# https://python-poetry.org/docs#ci-recommendations
ARG POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_HOME}/bin"
# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache
# Creating a virtual environment just for poetry and install it with pip
RUN python -m venv $POETRY_HOME \
    && $POETRY_HOME/bin/pip install poetry==${POETRY_VERSION}
# Copy Dependencies
COPY poetry.lock pyproject.toml README.md ./
COPY scripts scripts
COPY src src
# Validate the project is properly configured
RUN poetry check
RUN sh scripts/install.sh
CMD ["sh", "scripts/run-server.sh"]
