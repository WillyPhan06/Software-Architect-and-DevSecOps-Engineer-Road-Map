# Use official Python slim image
FROM python:3.12-slim

# set workdir
WORKDIR /app

# install build deps for any wheels (optional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# copy dependency files first for layer caching
COPY requirements.txt .

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# create a non-root user
RUN useradd --create-home appuser
USER appuser

# expose port (informational)
EXPOSE 8000

# healthcheck (container manager can use this)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request, sys
try:
  urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)
  sys.exit(0)
except:
  sys.exit(1)" || exit 1

# Run with Gunicorn using Uvicorn workers, binding to 0.0.0.0
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "--access-logfile", "-"]
