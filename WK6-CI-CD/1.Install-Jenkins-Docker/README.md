# Description

This is to guide how to install Jenkins locally.

# Pre-requisite

Docker

# Steps

## 1. Create a folder to hold Jenkins data

```
mkdir jenkins_home
cd jenkins_home
```

## 2. Start a Jenkins container
```
docker run --name jenkins \
           -u 0:$GID \
           -d \
           -v $(pwd):/var/jenkins_home \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -p 80:8080 \
           -p 50000:50000 \
           jenkinsci/blueocean
```
Note:
- `-u 0:$GID` specifies UID and GID of the user in Jenkins.
- `-d` detaches the container
- `-v $(pwd):/var/jenkins_home` mounts the current directory to Jenkins home inside the container
- `-v /var/run/docker.sock:/var/run/docker.sock` mounts Docker socks
- `-p 80:8080` maps port 80 in the host to port 8080 inside the container
- `-p 50000:50000` maps ports 50000 which is the default port for slave registration
- `jenkinsci/blueocean` is the image maintained by `jenkinsci`.

## 3. Open http://127.0.0.1 and you should see screen below
![Alt text](images/docker-install-01.png?raw=true)

## 4. Get your password by opening `secrets/initialAdminPassword` file in the directory you created in the first step.
```
cat secrets/initialAdminPassword
```

## 5. Continue installation in step #3 with password from step #4.

You should see screen below after full installation.
![Alt text](images/docker-install-02.png?raw=true)
