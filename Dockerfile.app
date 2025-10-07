# ==========================
# 🧱 Build Stage
# ==========================
FROM ghcr.io/astral-sh/uv:python3.13-bookworm AS builder

WORKDIR /app

# Copy only dependency metadata first for caching
COPY pyproject.toml ./
RUN touch README.md

# Install only the "serve" dependency group for production runtime
RUN uv sync --no-default-groups --group serve

# ==========================
# 🚀 Runtime Stage
# ==========================
FROM python:3.13-slim AS runtime

WORKDIR /app

# Create a non-root user for security
RUN addgroup --gid 1001 --system gunicorn && \
    adduser --system gunicorn --uid 1001 --gid 1001

# Copy project metadata and environment
COPY pyproject.toml .

# Set up virtual environment paths
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

# Copy the virtual environment from the builder stage
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copy your application source
COPY project_name project_name

# Copy Gunicorn configuration
COPY gunicorn.conf.py .

# Create writable instance directory (e.g., for SQLite or logs)
RUN mkdir instance && \
    chgrp gunicorn -R . && \
    chmod 750 -R . && \
    chmod 770 instance

USER gunicorn

EXPOSE 8000

ENV GUNICORN_WORKERS=1

# ==========================
# 🦄 Entry Point
# ==========================
# Use Gunicorn with Uvicorn worker for ASGI (FastAPI)
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "project_name.main:app", "-c", "gunicorn.conf.py"]
