# Description

This is a very simple example to dockerise a python flask application.

# TLDR;
```
./run.sh
```

# Build
Build a image named `jr/web-python-flask`.
```
cd 3.web-sitematcher

docker build -t jr/web-citymatcher .
```

# Run

```
docker run --name citymatcher -d --rm -p 80:80 jr/web-citymatcher
```
Note: 
- Use `--rm` option to remove container automatically. 
- Use `-d` to detach from the console.
- Use `--name` to specify container name.

In the browser, open http://localhost/?city=jin and you will get a list of cities that has "jin" in their name.

![Alt text](sample.png?raw=true)

You can also try any other URLs like http://localhost/?city=a
