#!/bin/bash
set -e

docker swarm leave --force | cat

# remove all the containers
docker ps -q | xargs -r docker kill
docker ps -qa | xargs -r docker rm
