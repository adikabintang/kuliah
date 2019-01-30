#!/bin/bash
HTTP_VERSION=$1
if [ $HTTP_VERSION = "2" ]
then
    export GODEBUG=http2server=1
    go run server.go
elif [ $HTTP_VERSION = "1" ]
then
    export GODEBUG=http2server=0
    go run server.go
fi

echo "Error: choose http version"
