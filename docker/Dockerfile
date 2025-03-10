FROM python:3.8

WORKDIR /app

# Install build dependencies
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

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]