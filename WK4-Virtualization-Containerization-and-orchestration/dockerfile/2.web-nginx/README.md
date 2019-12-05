# Description

This is a very simple example to dockerise a web application.

# TLDR;
```
./run.sh
```

# Build
Build a image named `jr/web-nginx`.
```
cd 2.web-nginx

docker build -t jr/web-helloworld .

docker images
```

# Run

```
docker run --rm -p 80:80 jr/web-helloworld
```
Note: Use `--rm` option to remove container automatically.

In the browser, open http://localhost and you will get a static web page.

![Alt text](sample.png?raw=true)

# Cleanup
Ctrl+C to stop the current container.
