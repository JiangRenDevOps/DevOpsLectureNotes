# Description

This is to demo how to use docker-compose to manage multiple services.

# TLDR;
```
./run.sh
```
# Install docker compose
```
./install-docker-compose.sh
```

# Build
Build all the Dockerfiles.
```
docker-compose build
```

# Run
Run all the containers with dependencies.
```
docker-compose up
```
- You can use http://localhost?city=au to use citymatcher
- You can use http://localhost:8080 to use nginx static website

![Alt text](sample.png?raw=true)

# Cleanup
Ctrl+C to stop 

or 
```
docker-compose down
```
