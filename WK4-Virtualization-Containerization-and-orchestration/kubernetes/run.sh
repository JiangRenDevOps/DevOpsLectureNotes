#!/bin/bash
set -e

cd scripts

if ! type "kind" 2>&1 > /dev/null ; then
    ./install-kind-and-kubectl.sh
fi

./delete-cluster.sh
./create-cluster.sh

./deploy-demoapp.sh
./deploy-dashboard.sh
