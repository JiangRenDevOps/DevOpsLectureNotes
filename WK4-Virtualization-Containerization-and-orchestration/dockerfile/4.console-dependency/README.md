# Description

This is a very simple example to dockerise a console application.

# TLDR;
```
./run.sh
```

# Build
Build a image named `jr/console-citymatcher`.
```
cd 4.console-dependency

docker build -t jr/console-citymatcher .
```

# Run

```
docker run --link citymatcher --rm jr/console-citymatcher
```
Note: 
- Use `--link` option to link a another container.
- Use `--rm` option to remove container automatically.

![Alt text](sample.png?raw=true)

# Cleanup
Just simply kill all the containers simply.
```
docker kill $(docker ps -q)
```