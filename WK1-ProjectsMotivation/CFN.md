# Description

This is to demo how we can create Cloudfront infrastructure via CLoudformation automatically.

# Pre-requisite

AWS Account

# Task 1: Login to AWS Cloudformation console
Open https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template

# Task 2: Create stack

1. Click "Create Stack" and select "With new resources (Standard)"
![Alt text](images/CFN1.png?raw=true)
2. Choose to upload template and select [CDN.yaml](https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK1-ProjectsMotivation/templates/cloudformation/CDN.yaml) file from our DevOpsLectureNotes repo. If you haven't cloned the repo, you can download the raw file and upload it.
![Alt text](images/CFN2.png?raw=true)
3. Input stack name and comment and click Next
![Alt text](images/CFN3.png?raw=true)
4. Scroll down and click "Next"
![Alt text](images/CFN4.png?raw=true)
5. Scroll down and click "Create Stack"
![Alt text](images/CFN5.png?raw=true)
6. You will be able to see Cloudfront distribution in the cloudfront console: https://console.aws.amazon.com/cloudfront/home
7. You can find cloudfront URL in the output tab once the stack is created.
![Alt text](images/CFN6.png?raw=true)
