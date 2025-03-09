FROM python:3.8

WORKDIR /app

COPY ./app/ /app

# Add these lines before installing dependencies
RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

RUN python -m spacy download en_core_web_sm
