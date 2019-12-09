#!/bin/bash

set -e

# https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta6/aio/deploy/recommended.yaml

kubectl apply -f config/dashboard-adminuser.yaml

token=$(kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}') | grep 'token:' | cut -d ':' -f 2 | sed 's# ##g')

url='http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login'


echo '####################################################################################'
echo "Please login to ${url}"
echo 
echo "Token: ${token}"
echo '####################################################################################'
kubectl proxy