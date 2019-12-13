#!/bin/bash
set -e

# deploy ingress controller
kubectl apply -f https://projectcontour.io/quickstart/contour.yaml

# https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
kubectl apply -f config/demoapp.yaml

kubectl get -n jiangren svc demoapp
kubectl describe -n jiangren svc demoapp

echo '#########################################################'
echo 'demoapp will be available in a minute. http://localhost'
echo '#########################################################'