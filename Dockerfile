# --- Builder Stage ---
FROM python:3.10-slim-bookworm AS builder

# Instala o Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.8.2
ENV PATH=$POETRY_HOME/bin:$PATH

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

# Configura o ambiente virtual dentro do builder
WORKDIR /app
COPY pyproject.toml poetry.lock* ./

# Instala as dependências, excluindo as de desenvolvimento
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-interaction --no-ansi

# --- Runtime Stage ---
FROM python:3.10-slim-bookworm AS runtime

WORKDIR /app

# Copia o ambiente virtual do builder
COPY --from=builder /app/.venv ./.venv

# Ativa o ambiente virtual para os comandos subsequentes
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código-fonte da aplicação
COPY src/ ./src

# Define o comando padrão para executar a aplicação
CMD ["python", "src/main.py"]
