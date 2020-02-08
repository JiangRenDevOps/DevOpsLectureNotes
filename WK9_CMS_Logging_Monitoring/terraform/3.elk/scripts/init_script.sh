#!/bin/bash
set -e

apt update

apt install -y ansible

ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.pip

ansible_playbook=/site.yaml
wget https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK9_CMS_Logging_Monitoring/terraform/3.elk/scripts/site.yaml -O $ansible_playbook

ansible-playbook $ansible_playbook
