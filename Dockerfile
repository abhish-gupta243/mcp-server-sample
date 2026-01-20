FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# Expose the port (8000 is default for many Python apps)
EXPOSE 8000

# Run the server
CMD ["python", "server.py"]