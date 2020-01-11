# Description

This is to demo the generic usage of Ansible.

# Tasks

## Task #1: Install Ansible
Install Ansible, boto3 and botocore via pip3. We install boto3 because it's required by Ansible Inventory EC2 plugin. 
```
pip3 install ansible boto3 botocore
```
Validate by executing `ansible --version` and check it's using python3.

Alternatively, you can follow https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

## Task #2: Create AWS EC2 instances in us-east-1 region to test
- Please create a ssh key in AWS. Suggest to import your ssh public key below directly.
```
cat ~/.ssh/id_rsa.pub
```
- Use this [cloudformation template](CFN-EC2.yaml) to create three EC2 instances.

## Task #3: Create an IAM user and configure two environment variables
Get the value from your AWS console.
```
export AWS_ACCESS_KEY=YOUR_AWS_ACCESS_KEY
export AWS_SECRET_KEY=YOUR_AWS_SECRET_KEY
```

## Task #4: Run hello world to validate the setup of the EC2 instances
```
cd DevOpsLectureNotes/WK7-CM-Ansible/ansible-playbooks
ansible all -i inventory.aws_ec2.yaml -u ubuntu -m ping
```

## Task #5: Install a docker role from galaxy to your local laptop
```
ansible-galaxy install geerlingguy.docker
```

Alternatively, you can use `ansible-galaxy install -f requirements.yaml`

## Task #6: Read playbook under ansible-playbook-plain and execute
Read `site.yaml` under `ansible-playbook-plain`.
```
ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
```

## Task #7: Read playbook under ansible-playbook-roles and execute
Read `site.yaml` under `ansible-playbook-roles`.
```
ansible-playbook -i ../inventory.aws_ec2.yaml site.yaml
```

## Task #8: Install more software via Ansible and play around
Install sth like Jenkins, Kubernetes, wordpress, nginx etc.
