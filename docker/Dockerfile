FROM python:3.8-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Explicitly set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=main.py

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "main.py"]