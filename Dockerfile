FROM python:3.10-alpine as build

WORKDIR /app
COPY . /app


RUN pip install -r requirements.txt
