FROM python:3.10-alpine3.20

ENV PYTHONUNBUFFERED 1

WORKDIR /spycats

ENV PYTHONPATH=${PYTHONPATH}:/spycats/management/commands

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
