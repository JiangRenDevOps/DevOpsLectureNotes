#!/bin/bash

cd "$(dirname "$0")"


if [ "$(docker-compose --version 2>/dev/null)" == "" ]; then
    echo "docker-compose not found. Installing it ..."
    ./install-docker-compose.sh
fi

# Clean up
docker ps -q | xargs -r docker kill
docker ps -qa | xargs -r docker rm

# Start compose
docker-compose up
