#!/bin/bash
set -e 

while true; do
    echo
    echo "##################################"
    ssh ec2-user@54.206.36.48 ls
    echo "##################################"
    sleep 1
done