# Statsd

Instead of Prometheus scraping our Python web application directly, we will let each worker process push its metrics to a certain “bridge” application, which will then convert these individual data points into aggregated metrics. These aggregated metrics will then be converted into Prometheus metrics when Prometheus queries the bridge.

## Statsd Exporter

This “bridge” application here is the `statsd exporter`. The idea is that we will modify our middleware `app_helper` module to push the metrics in a [statsd] compatible format to this bridge instead:
```
[Python Web application Worker]   \

[Python Web application Worker]   - > [Statsd Exporter]    <- [Prometheus]

[Python Web application Worker]   /

```


## Hands on

Let us build our app
```
cd flask_statsd_prometheus
docker build -t jr/flask_app_statsd .
```
verify it can run

```
docker run  -ti -p 5000:5000 -v `pwd`/src:/application jr/flask_app_statsd 
```
Stop existing running dockers
```
docker rm webapp 
docker rm prometheus
```

Docker-compose up now
```
docker-compose -f docker-compose.yml -f docker-compose-infra.yml up
```

Hit some endpoints at `locahost:5000` and try the following query `localhost:9090/graph`
```
request_count
```

Now, you wouldn't see a problem with request count drop. 

