python official image hub:

http://hub.docker.com/_/python

## Docker step by step

### Step 1. Pull the official python docker image

```
docker pull python:3.7-alpine
```

### Step 2. Run the docker container with interactive mode

``` 
docker run -it --name python37 --rm python:3.7-alpine /bin/sh 
```

### Step 3. Enter the container and check the python version

``` 
python --version 
```

### Optional Steps. If the download is not fast enough, try set up another source.

set pip aliyun mirror source
```
mkdir $HOME/.pip/
   
   tee $HOME/.pip/pip.conf <<-'EOF'
   [global]
   trusted-host=mirrors.aliyun.com
   index-url=https://mirrors.aliyun.com/pypi/simple
   EOF
```
python uses alpine system

alpine uses apk package management

命令如下：

```
apk add

apk update

apk del
```
Set alpine mirror source

```
echo http://mirrors.ustc.edu.cn/alpine/v3.7/main > /etc/apk/repositories
   
echo http://mirrors.ustc.edu.cn/alpine/v3.7/community >> /etc/apk/repositories
```
Update the packages
```
apk update && apk upgrade
```

### Step 4. Install Flask
```
python -m pip install -U flask
```

### Step 5. Write the app.py
### Step 6. Run it 
```
python app.py
```
or 
```
export FLASK_APP=/test.py

flask run
```
### Step 7. Validate it
```
docker exec -it python37 /bin/sh
```
```
apk add curl
```
```
curl localhost:5000
   
curl localhost:5000/abc
```
## Dockerfile

Of course, we could write everything in a dockerfile
See Dockerfile

### Step 1. Build the docker image
```
docker build -t my_docker_flask:latest .
```
### Step 2. Run docker 
```
docker run -d -p 5000:5000 my_docker_flask:latest
```
### Step 3. Check host
```
http://127.0.0.1:5000
```
Enter the above URL in the host browser. This should return you "Hello World"

### Step 4. Set up load balancer
 
 
### Step 5. Docker Compose
docker-compose up -d : run containers in background 

docker-compose stop: stop all containers

docker-compose down: delete all containers but keep the volumes

docker-compose ps：show the current status