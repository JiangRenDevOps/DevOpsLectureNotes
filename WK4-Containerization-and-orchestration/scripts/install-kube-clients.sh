#!/bin/bash
set -e

echo "Installing cubectl ..."
sudo snap install kubectl --classic

echo "Installing aws-iam-authenticator ..."
sudo snap install go --classic
go get -u -v sigs.k8s.io/aws-iam-authenticator/cmd/aws-iam-authenticator 

