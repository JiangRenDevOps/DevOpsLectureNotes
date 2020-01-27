# Grafana
Grafana is the open source analytics and monitoring solution for every database

![Alt text](./images/grafana.png?raw=true)

## Hands-on
Let us open `localhost:3000`

Use the username `admin` and password `foobar`

Let us add the resource for our dashboard

We need to set the promethus server:
```
http://prometheus:9090
```

Let us set the scrape interval to be `1s`. Don't set it to 1s in prod, as it will overwhelm your service.

Check out the `request_count` metrics.

 

