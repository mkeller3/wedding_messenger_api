FROM ubuntu:20.04

RUN mkdir /app

WORKDIR /app

ADD . /app/

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1
ENV PORT=8888

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip3 install -r requirements.txt
EXPOSE 8888

CMD gunicorn wedding_messegner.wsgi:application --bind 0.0.0.0:8888 --timeout 320 --workers 5