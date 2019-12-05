#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "Building image ..."
docker build -t jr/web-helloworld .

echo
echo "Running container ..."
echo "Please open http://localhost to view resource served by the container."
docker run --rm -p 80:80 jr/web-helloworld
