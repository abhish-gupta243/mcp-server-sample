FROM registry.access.redhat.com/ubi9/python-311
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py .

EXPOSE 8000

# Use gunicorn with uvicorn worker - no host validation
CMD ["gunicorn", "server:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--forwarded-allow-ips", "*"]