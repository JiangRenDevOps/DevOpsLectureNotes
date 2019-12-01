#!/bin/bash

cd "$(dirname "$0")"


if [ "$(docker-compose --version 2>/dev/null)" == "" ]; then
    echo "docker-compose not found. Installing it ..."
    ./install-docker-compose.sh
fi

# Clean up
docker kill $(docker ps -q)
docker rm $(docker ps -aq)

# Start compose
docker-compose up
