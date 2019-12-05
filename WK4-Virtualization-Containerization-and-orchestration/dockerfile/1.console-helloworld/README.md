# Description

This is a very simple example to dockerise a console application.

# TLDR;
```
./run.sh
```

# Build
Build a image named `jr/console-helloworld`.
```
cd 1.console-helloworld

docker build -t jr/console-helloworld .

docker images
```

# Run

```
docker run --rm jr/console-helloworld
```
Note: Use `--rm` option to remove container automatically.
