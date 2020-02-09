#!/bin/bash
set -e

apt update

apt install -y ansible

ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.pip
ansible-galaxy install geerlingguy.filebeat

ansible_playbook=/site.yaml
wget https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK9_CMS_Logging_Monitoring/terraform/4.app/scripts/site.yaml -O $ansible_playbook

sed -i 's/ELK_IP/ELK_IP_PLACEHOLDER/g' site.yaml

# try three times to work around an issue in geerlingguy.filebeat
for i in 1 2 3; do
    sudo ansible-playbook $ansible_playbook | cat
done
