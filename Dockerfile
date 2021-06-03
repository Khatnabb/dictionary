FROM python:3.8

WORKDIR /app
ADD requirements.txt /app

RUN pip3 install -U -r requirements.txt
