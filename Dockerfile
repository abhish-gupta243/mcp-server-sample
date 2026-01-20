FROM registry.access.redhat.com/ubi9/python-311
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py .

EXPOSE 8000

# Critical: Add --no-server-header flag to bypass validation
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--forwarded-allow-ips", "*", "--proxy-headers"]