FROM python:3.7.2-alpine3.9
ADD . /sub
WORKDIR /sub
RUN mkdir -p /sub/output_db
RUN apk update \
    && apk add sqlite \
    && apk add socat
RUN pip install --upgrade pip
RUN pip install paho-mqtt
CMD ["python", "subs_v2.py"]