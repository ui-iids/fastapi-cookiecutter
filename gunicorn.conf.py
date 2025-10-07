from os import environ

# Your FastAPI application’s import path
# Example: app/main.py defines "app = FastAPI()"

# Use the uvicorn worker class for ASGI
worker_class = "uvicorn.workers.UvicornWorker"

# The ASGI app import path
# e.g., app/main.py → app:app
# If your app is in project_name/main.py, use:
# "project_name.main:app"
app_module = environ.get("FASTAPI_APP", "project_name.main:app")

# Gunicorn configuration
bind = "0.0.0.0:8000"
workers = int(environ.get("GUNICORN_WORKERS", 1))
timeout = 120  # optional: useful for long-running requests

# Use 'command' override in CLI if needed:
# gunicorn -c gunicorn.conf.py project_name.main:app
