FROM python:3.7.2-alpine3.9
ADD . /pub
WORKDIR /pub
RUN pip install --upgrade pip
RUN pip install paho-mqtt
CMD ["python", "pub_v2.py"]