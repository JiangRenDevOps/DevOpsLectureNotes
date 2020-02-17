# High Availability
High availability refers to systems that are durable and likely to operate continuously without failure for a long time. The term implies that parts of a system have been fully tested and, in many cases, that there are accommodations for failure in the form of redundant components.

# Failover
https://docs.rightscale.com/cm/designers_guide/cm-designing-and-deploying-high-availability-websites.html


# Hands-on
Voting App Example 1
https://github.com/docker/swarm-microservice-demo-v1

Let us try to understand what does it do and how to spin it up.


How would high availability help the App?


What other problems do you see with the App? Is it 100% available now? How to improve?

Voting App Example 2
https://github.com/dockersamples/example-voting-app


# Kind and Kubectl
kind is a tool for running local Kubernetes clusters using Docker container “nodes”.
https://kind.sigs.k8s.io/

Prerequisite 
```
go get -u sigs.k8s.io/kind
```
install kind
```
kind create cluster
```
verify 

```
kind get cluster
```

```
kubectl cluster-info
```

# Autoscaling
```
git clone https://github.com/dockersamples/example-voting-app
```
create namespace
```
kubectl create namespace vote                                                           
```
You should see
```
namespace/vote created
```

Now let us create the cluster
```
kubectl create -f k8s-specifications/                                                    ✓  10780  23:22:42
```
It should return
```
deployment.apps/db created
service/db created
deployment.apps/redis created
service/redis created
deployment.apps/result created
service/result created
deployment.apps/vote created
service/vote created
deployment.apps/worker created
```

Check the status
```
kubectl get pods --namespace=vote --output=wide
kubectl get services --namespace=vote
```
You will probably see an error for postgres `CrashLoopBackOff`

Let us check the error
```
kubectl logs <NAME> --namespace=vote
```
This was because a recent upgrade of postgres and we have to pass in the postgres password, even it is the default one.
Let us specify the password by adding the following in the `db-deployment.yml`
```
        env:
        - name: POSTGRES_PASSWORD
          value: password
```
You should also see some errors here:
```
kubectl describe pods --namespace=vote
```

Let us stop everything
``` 
kubectl delete deployment hello-world
kubectl delete service hello-world
kubectl delete --all pods
kubectl delete namespace vote
```
and restart them:
```
kubectl create -f k8s-specifications/
```
Since we are not on google cloud and don't have a loadbalancer setup, we can port forward to access our app:
```
kubectl port-forward -n vote svc/vote --namespace=vote 5000:5000
```

```
kubectl port-forward -n vote svc/result --namespace=vote 5001:5001
```

Now let us try to access localhost:5000 and 5001

Also, try to understand what does these mean:
```
kubectl get pods --namespace=vote --output=wide
kubectl get svc --namespace=vote
kubectl get deployments --namespace=vote

```

Try to delete a pod and see if it gets deleted:
```
What command should we use?
```
###Manual Scaling
You can set the replicas to higher number and it should generate more nodes for each deployment.
You can also scale the nodes manually. Are you able to find the command?

###Auto Scaling
Let us set the Auto Scaling Policy for our nodes
```
kubectl autoscale deployment vote --namespace=vote --cpu-percent=50 --min=1 --max=10
```
check the settings:
```
kubectl get hpa --namespace=vote
```

Let us check what is wrong?
Did you see `<unknown>/50%`?
```
kubectl describe hpa --namespace=vote
kubectl get -n kube-system pods
kubectl -n kube-system logs <pod>
```

To fix it,
1. Clone metrics-server with `git clone https://github.com/kubernetes-incubator/metrics-server.git`
2. Edit deploy/kubernetes/metrics-server-deployment.yaml and add these:
```
containers:
- name: metrics-server
    image: k8s.gcr.io/metrics-server-amd64:v0.3.1
    command:
      - /metrics-server
      - --kubelet-insecure-tls
      - --kubelet-preferred-address-types=InternalIP
``` 
3 . Create the resource
```
kubectl create -f deploy/kubernetes
```
4 . Delete the old hpa:
```
kubectl delete hpa --all --namespace=vote
```
5 . Stop the current app:
```
kubectl delete -f k8s-specifications/
``` 
6 . Add the following to `vote-deployment.yaml` under container
```
        resources:
          limits:
            cpu: 20m
          requests:
            cpu: 10m
```
7 . Recreate everything:
```
kubectl create -f k8s-specifications/
``` 
8 . Recreate asg rule:
```
kubectl autoscale deployment vote --namespace=vote --cpu-percent=50 --min=1 --max=10
```
You should now see
```
↳ kubectl get hpa --namespace=vote                                                         ✓  11177  00:05:40
NAME   REFERENCE         TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
vote   Deployment/vote   0%/50%     1         10        1          38s
```





####Other commands and some references

```
kubectl get deployments
kubectl get deployments --namespace=vote
```
We need to delete the deployments before delete all the pods
```
kubectl delete deployment hello-world
kubectl delete service hello-world
kubectl delete --all pods
```
https://itnext.io/starting-local-kubernetes-using-kind-and-docker-c6089acfc1c0

