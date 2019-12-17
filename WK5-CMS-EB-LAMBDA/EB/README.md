# Description

This is to demo how we can deploy a sample application to Elastic Beanstalk

# Tasks

## Task #1: Create a Redis cluster

### Step 1: Login to AWS Cloudformation console
Login to https://console.aws.amazon.com/cloudformation/home?region=us-east-1

Note: Please don't use Sydney region (ap-southeast-2) because it's covered by free tier and we need to pay for it. See: https://aws.amazon.com/about-aws/whats-new/2013/03/05/amazon-elasticache-aws-free-tier/

### Step 2: Create Cloudformation stack
The cloudformation template is here:
https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK5-CMS-EB-LAMBDA/EB/cfn-redis.yaml

Input stack name and select "subnets" as well as "VPC". Use all default settings for the rest steps.

![Alt text](images/EB01.png?raw=true)

## Step 3: Get the Redis Host name
You can get Redis Host name from two different places.

1. The output of Cloudformation stack;

2. Elasticache Redis console: https://console.aws.amazon.com/elasticache/home?region=us-east-1#redis:

The redis host name will be used in the next task.
![Alt text](images/EB08.png?raw=true)

Note: In our real life, we should use a custom domain name in route53 to bind to the redis cluster.

## Task #2: Create an Elastic Beanstalk application and environment

### Step 1: Create an application
Open Elastic Beanstalk Console: https://console.aws.amazon.com/elasticbeanstalk/home?region=us-east-1#/applications and create.

### Step 2: Create an environment
Choose "Web server environment" and "Docker" as platform.

![Alt text](images/EB04.png?raw=true)

Click Upload button.
![Alt text](images/EB03.png?raw=true)

We need to zip our application folder and upload it. Please make sure Dockerfile is in the root of the zip file.
![Alt text](images/EB02.png?raw=true)

The creation will take a few minutes. After this step, we should be able to view the app. However, we won't be able to store data or load data.

![Alt text](images/EB05.png?raw=true)

### Step 3: Configure REDIS_HOST environment variable
Click "Configuration" tab and Modify "Software" configuration. 

![Alt text](images/EB06.png?raw=true)

In the bottom of the configuration page, you should be able to add `REDIS_HOST` environment variable.


![Alt text](images/EB07.png?raw=true)
After saving, it will take a bit time for Elastic Beanstalk to apply the change.

Now you should be able to use the application as normal.


![Alt text](images/EB09.png?raw=true)

### (Optional) Play around

You can try to 
- clone an environment
- swap DNS
- view application logs