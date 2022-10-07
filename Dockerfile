FROM tiangolo/uvicorn-gunicorn:python3.8-slim

LABEL maintainer="team-erc"

ENV WORKERS_PER_CORE=4
ENV MAX_WORKERS=24
ENV LOG_LEVEL="warning"
ENV TIMEOUT="200"

WORKDIR /opt

COPY requirements.txt ./
COPY src/ /opt/src
COPY yolov5/ /opt/yolov5

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install -r /opt/yolov5/requirements.txt

RUN apt-get update && apt-get install -y python3-opencv git