#!/bin/bash
set -e

# Reset docker
docker swarm leave --force
docker kill $(docker ps -q)
docker rm $(docker ps -aq)

# init swarm
docker swarm init

# Get join token:
SWARM_TOKEN=$(docker swarm join-token -q worker)
echo $SWARM_TOKEN

# Get Swarm master IP (Docker for Mac xhyve VM IP)
SWARM_MASTER_IP=$(docker info | grep -w 'Node Address' | awk '{print $3}')
echo $SWARM_MASTER_IP

# Number of workers
NUM_WORKERS=3
# Docker version
DOCKER_VERSION=17.09.1-ce-dind

# Run NUM_WORKERS workers with SWARM_TOKEN
for i in $(seq "${NUM_WORKERS}"); do
	docker run -d --privileged --name worker-${i} --hostname=worker-${i} -p ${i}2375:2375 docker:${DOCKER_VERSION}
	docker --host=localhost:${i}2375 swarm join --token ${SWARM_TOKEN} ${SWARM_MASTER_IP}:2377
done

# Create visualizer
docker service create \
  --name=viz \
  --publish=8080:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer

docker node ls

docker stack deploy -c docker-compose.yaml myswarm

docker service ls

# 
# docker service ps 
# docker swarm leave --force