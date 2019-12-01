#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "Building image ..."
docker build -t jr/console-citymatcher .

echo
echo "Running container ..."
docker run -it --link citymatcher --rm jr/console-citymatcher

echo "Cleaning up ..."
docker kill $(docker ps -q)
docker rm $(docker ps -aq)
