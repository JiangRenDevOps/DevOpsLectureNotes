#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "Building image ..."
docker build -t jr/web-citymatcher .

echo
echo "Running container ..."
echo "Please open http://localhost?city=au to search cities whose name contains 'au'."
docker run --name citymatcher -d --rm -p 80:80 jr/web-citymatcher
