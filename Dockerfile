FROM tiangolo/uvicorn-gunicorn:python3.8-slim
ARG HOST
ARG PORT
LABEL maintainer="team-erc"

ENV HOST=${HOST}
ENV PORT=${PORT}
ENV WORKERS_PER_CORE=4
ENV MAX_WORKERS=24
ENV LOG_LEVEL="warning"
ENV TIMEOUT="200"

WORKDIR /opt

COPY requirements.txt ./
COPY src/ /opt/src
COPY yolov5/ /opt/yolov5
COPY trackers/ /opt/trackers
COPY best.pt /opt/best.pt
COPY track.py /opt/track.py
COPY test_video /opt/test_video
COPY NMEA_111122.log /opt/NMEA_111122.log

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install -r /opt/yolov5/requirements.txt

RUN apt-get update && apt-get install -y python3-opencv git

RUN echo $HOST
RUN echo $PORT

#CMD python track.py --source  test_video/2021-11-22_11-27-22-_online-video-cutter.com_.mp4 --yolo-weights best.pt --img 640 --tracking-method strongsort --save-vid --conf-thres 0.7 --reid-weights osnet_x1_0_msmt17.pt
CMD python track.py --source  rtsp://admin:admin@192.168.1.13:554/stander/livestream/0/0 --yolo-weights best.pt --img 640 --tracking-method strongsort --save-vid --conf-thres 0.7 --reid-weights osnet_x1_0_msmt17.pt --host $HOST --port $PORT