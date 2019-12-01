#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "Building image ..."
docker build -t jr/console-helloworld .

echo
echo "Running container ..."
docker run --rm jr/console-helloworld
