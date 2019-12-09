#!/bin/bash

cd "$(dirname "$0")"

./scripts/delete-cluster.sh

# remove all the containers
docker ps -q | xargs -r docker kill
docker ps -qa | xargs -r docker rm
