# Description
This is a sample answer for the homework of the 2nd lecture.

# Task #1: Cloudformation CLI
## Question
Configure AWS credentials in your local laptop and use AWS CLI to create a cloudformation stack “CDN.yaml” in aws cli command line.
Tips: read and follow the guidelines in “Quickly Configuring the AWS CLI” section: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

You will need to give cloudformation and cloudfront permissions. Or you can start with attach an “Admin” permission (security risk and anti-pattern).

## Short Answer
Configure AWS credential and execute command below to create a stack.
```
aws cloudformation create-stack --stack-name My-CDN-Stack --template-body file://CDN.yaml --parameters ParameterKey=CommentParameter,ParameterValue=FromAWSCLI
```
## Long Answer
1. Login to IAM user: https://console.aws.amazon.com/iam/home?region=ap-southeast-2#/users and click "Add user" button;
![Alt text](images/HOMEWORK1.png?raw=true)
2. Input user name and tick "Programmatic access" checkbox to allow AWS CLI to use it;
![Alt text](images/HOMEWORK2.png?raw=true)
3. Select "Attach existing policies directly", you can either create your own policy or select existing policy that satisfy your task. In this example, I choose "AdministratorAccess" to simplify the permission setting but do remember this is anti-pattern and you should never do this in your work or production environment.
![Alt text](images/HOMEWORK3.png?raw=true)
4. [optional] Add tags as you need;
![Alt text](images/HOMEWORK4.png?raw=true)
5. Review the setting and click "Create user".
![Alt text](images/HOMEWORK5.png?raw=true)
6. Now, you get "Access Key ID" and "Secret access key". You need to click a "show" link to view the "Secret access key".
![Alt text](images/HOMEWORK6.png?raw=true)
7. Open terminal and execute `aws configure` command. If you don't have "aws cli", please install through this [AWS User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
![Alt text](images/HOMEWORK7.png?raw=true)
8. Now, you can use AWS CLI to create a cloudformation stack. Make sure you have [CDN.yaml](https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK1-ProjectsMotivation/templates/cloudformation/CDN.yaml). file in your current directory and execute `
aws cloudformation create-stack --stack-name My-CDN-Stack --template-body file://CDN.yaml --parameters ParameterKey=CommentParameter,ParameterValue=FromAWSCLI
`.
![Alt text](images/HOMEWORK8.png?raw=true)
9. You can find a stack is under creation in cloudformation console: https://ap-southeast-2.console.aws.amazon.com/cloudformation/home
![Alt text](images/HOMEWORK9.png?raw=true)
10. Wait for a few minutes util the cloudformation stack is created.
![Alt text](images/HOMEWORK10.png?raw=true)
11. Check if the distribution in your cloudfront is successfully created.
![Alt text](images/HOMEWORK11.png?raw=true)

# Task 2: cloudformation template to create route53
## Question
Develop a Cloudformation template to create route53 hostzone and DNS records. The expectation is that you will create a hosted zone and a DNS record in the route53 via this cloudformation template..
Tips:
Create hosted zone: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
Create recordset:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
## Short Answer
https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK1-ProjectsMotivation/templates/cloudformation/DNS.yaml

## Long Answer
1. Download the cloudformation template [DNS](https://raw.githubusercontent.com/JiangRenDevOps/DevOpsLectureNotes/master/WK1-ProjectsMotivation/templates/cloudformation/DNS.yaml) and have a read. There are two resources. One is Route53 Hosted zone and anther one is Recordset.
2. Create a cloudformation stack in command line via `aws cloudformation create-stack --stack-name My-DNS-Stack --template-body file://DNS.yaml --parameters ParameterKey=YourDomainNameParameter,ParameterValue=your_name.jiangren.mooo.com`
![Alt text](images/HOMEWORK12.png?raw=true)
3. In the [Route53 console](https://console.aws.amazon.com/route53/home?region=ap-southeast-2), you will find a route53 hosted zone created with CNAME DNS record.
![Alt text](images/HOMEWORK13.png?raw=true)
4. Create a file with your Domain name and the content is value of NS record in Route53. Scp the file to the server to create DNS delegation: `scp your_name.jiangren.mooo.com ec2-user@54.206.36.48:/home/ec2-user`.
![Alt text](images/HOMEWORK14.png?raw=true)
5. You can validate your DNS record via dig command to your domain name: `dig www.your_name.jiangren.mooo.com`. 
![Alt text](images/HOMEWORK997.png?raw=true)
6. Now, you should be able to access a website with the route53 record you just created (with `www` prefix). Please note that we haven't created SSL certificate for the domain so we can only access by "http://" but not "https://". For example: http://www.your_name.jiangren.mooo.com The default target is http://jiangren.com.au since Jiangren website doesn't support anonymous CNAME alias. You will see a 404 page from Jiangren server and it's as expected because our CNAME is not added to the nginx server of Jiangren. Getting this message is enough for our test.
![Alt text](images/HOMEWORK998.png?raw=true)
7. Do remember to delete the route53 hosted zone by deleting cloudformation stack so you won't be charged by Route53 hosted zone!!!
![Alt text](images/HOMEWORK999.png?raw=true)

# Task #3: Apply a domain name
## Question
(Optional) Apply a domain name and play around
It can be a free sub-domain name or a free/paid TLD domain name.
Tips: try any of them or just search “Free domain name” in Google.
https://godaddy.com
https://onlydomains.com
https://namecheap.com
https://freedns.afraid.org (Free)

## Answer
Take freedns for example. 
1. Register a free account: http://freedns.afraid.org/pricing/
![Alt text](images/HOMEWORK17.png?raw=true)
2. Apply a free domain name
![Alt text](images/HOMEWORK16.png?raw=true)
3. You can find your domain in the subdomain list
![Alt text](images/HOMEWORK15.png?raw=true)
