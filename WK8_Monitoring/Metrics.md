## Metrics and metric types

For our purposes, a __metric__ is an observed value of a certain quantity at a given point in time. The total of number hits on a blog post, the total number of people attending a talk, the number of times the data was not found in the caching system, the number of logged-in users on your website—all are examples of metrics.

They broadly fall into three categories:

### Counters

Consider your personal blog. You just published a post and want to keep an eye on how many hits it gets over time, a number that can only increase. This is an example of a counter metric. Its value starts at 0 and increases during the lifetime of your blog post. Graphically, a counter looks like this:
![Alt text](./images/counter-graph.png?raw=true)
### Gauges
Instead of the total number of hits on your blog post over time, let's say you want to track the number of hits per day or per week. This metric is called a gauge and its value can go up or down. Graphically, a gauge looks like this:
![Alt text](./images/gauge-graph.png?raw=true)
A gauge's value usually has a ceiling and a floor in a certain time window.

### Histograms and timers
A histogram (as Prometheus calls it) or a timer (as StatsD calls it) is a metric to track sampled observations. Unlike a counter or a gauge, the value of a histogram metric doesn't necessarily show an up or down pattern. I know that doesn't make a lot of sense and may not seem different from a gauge. What's different is what you expect to do with histogram data compared to a gauge. Therefore, the monitoring system needs to know that a metric is a histogram type to allow you to do those things.
![Alt text](./images/histogram-graph.png?raw=true)