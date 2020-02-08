#!/bin/bash

wget  -o /home/ubuntu/site.yaml

pip3 install ansible
ansible-playbook localhost /home/ubuntu/site.yaml