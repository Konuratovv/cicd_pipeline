FROM python:latest

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

COPY requirements.txt .

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt