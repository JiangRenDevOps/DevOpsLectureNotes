#!/bin/bash
set -e

# https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
kubectl apply -f config/nginxdemos-service.yaml

kubectl get svc nginxdemos
kubectl describe svc nginxdemos
kubectl get ep nginxdemos