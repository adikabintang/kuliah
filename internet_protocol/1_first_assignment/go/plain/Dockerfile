FROM golang:1.11.5-alpine3.8

WORKDIR /app
RUN mkdir -p /app/file 
COPY serve* /app/
COPY templates/ /app/templates

EXPOSE 443
ENV GODEBUG=http2server=1
CMD ["go", "run", "server.go"]

# see docker inspect, see on networking