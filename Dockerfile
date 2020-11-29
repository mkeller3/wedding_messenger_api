FROM ubuntu:20.04

RUN mkdir /app

WORKDIR /app

ADD . /app/

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1
ENV PORT=8888

RUN apt-update && apt-add \
        python3-pip \
        python3-dev \
        python3-venv \
        && \
    rm -rf /var/lib/apt/lists*

RUN pip3 install - requirements.txt
EXPOSE 8888

CMD gunicorn wedding_messegner.wsgi:application --bind 0.0.0.0:8888 --timeout 320 --workers 5