FROM ubuntu:18.04

WORKDIR /app
ADD requirements.txt /app

RUN pip3 install -U -r requirements.txt
