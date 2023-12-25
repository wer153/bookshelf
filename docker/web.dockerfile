FROM python:3.11-slim-bookworm
WORKDIR /code
ENV PIPX_BIN_DIR="${HOME}/.local/bin"
ENV PATH="${PIPX_BIN_DIR}:${PATH}"
# Copy Dependencies
COPY poetry.lock pyproject.toml README.md ./
COPY app app
# Install Package Dependencies
RUN python -m pip install pipx && \
    pipx install poetry==1.7.1
RUN poetry check && poetry install --only main
ENTRYPOINT ["poetry", "run", "uvicorn", "--factory", "app.main:create_app", "--host", "0.0.0.0"]
