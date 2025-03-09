FROM python:3.10-slim

WORKDIR /app

# Install only the necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy application code
COPY ./app/ .
COPY ./ai_log_analysis/ /ai_log_analysis/

# Run the application
CMD ["python", "main.py"]