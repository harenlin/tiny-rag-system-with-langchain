# REMEMBER TO SET UP YOUR .env FILE FIRST!

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirement.txt

RUN python create_db.py

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3", "rag.py"]
CMD ["--query", "What is builder design pattern?"]
