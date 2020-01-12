# Configuration as code

Configuration as code (CAC) is managing configuration resources in your source repository. You treat your application config resources as versioned artifacts. By managing your application environment in tandem with your application code, you gain the same benefits you get with your code. 

# Architecture
A typical modern architecture would look like this

![Alt text](../images/architecture_overview.png?raw=true)
s3 - host static files

Cognito - authentication service

API Gateway - Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.
              
AWS Lambda -  AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you.

DynamoDB - NoSql Database Service

![Alt text](../images/simple_architecture.png?raw=true)

Now, it is time to build our infrastructure; Let us build our hello world lambda function with api gateway via terraform
 

# Preparation
Have AWS CLI installed
```
pip install awscli
```
Downloaded terraform v0.12.18 from terraform.io and moved this file to 
```
/usr/local/bin
```
```
$ terraform version                                                                                                             ✓  12129  17:40:08
Terraform v0.12.18
```
Set up your credentials `aws_access_key_id` and `aws_secret_access_key` in 
```
~/.aws/credentials
```
Since I have two different accounts, I named my personal profile goggle. But you can use the default one.
![Alt text](../images/aws_credentials.png?raw=true)

# Build and upload the lambda function to s3
In main.js, we have prepared a simple node js file
```
'use strict'

exports.handler = function(event, context, callback) {
    var response = {
        statusCode: 200,
        headers: {
            'Content-Type': 'text/html; charset=utf-8'
        },
        body: '<p>Bonjour au monde!</p>'
    }
    callback(null, response)
}
``` 
zip the file to example.zip
```
$ cd example
$ zip ../example.zip main.js
  adding: main.js (deflated 33%)
$ cd ..
```

create the s3; make sure you use a globally unique bucket name
![Alt text](../images/create_s3_via_awscli.png?raw=true)

upload the lambda function to s3
![Alt text](../images/copy_example_to_s3_via_awscli.png?raw=true)

## Build the configuration as code 

Let us start with setting up the main function. See
```
../staging/services/backend_app/main.tf
```
Provider - Set up the provider for our terraform
A provider is responsible for understanding API interactions and exposing resources. Providers generally are an IaaS (e.g. Alibaba Cloud, AWS, GCP, Microsoft Azure, OpenStack), PaaS (e.g. Heroku), or SaaS services (e.g. Terraform Cloud, DNSimple, CloudFlare).
https://www.terraform.io/docs/providers/index.html

Our provider is "aws"
```
provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "/Users/ywang/.aws/credentials"
  profile                 = "goggle"
}
```

Now let us set up the lambda function. See
```
../staging/services/backend_app/lambda.tf
```

Resource - Resources are the most important element in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks, compute instances, or higher-level components such as DNS records.

```
resource "aws_lambda_function" "example" {
  function_name = "ServerlessExample"

  # The bucket name as created earlier with "aws s3api create-bucket"
  s3_bucket = "terraform-serverless-yu-wang"
  s3_key    = "v1.0.0/example.zip"

  # "main" is the filename within the zip file (main.js) and "handler"
  # is the name of the property under which the handler function was
  # exported in that file.
  handler = "main.handler"
  runtime = "nodejs10.x"
  role=aws_iam_role.lambda_exec.arn
}
```
and this function
```
# IAM role which dictates what other AWS services the Lambda function
# may access.
resource "aws_iam_role" "lambda_exec" {
  name = "serverless_example_lambda"
  # Each Lambda function must have an associated IAM role which dictates what access it has to other AWS services.
  # The above configuration specifies a role with no access policy,
  # effectively giving the function no access to any AWS services,
  # since our example application requires no such access.
  assume_role_policy=<<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "lambda.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF

}
```

## terraform init
This command performs several different initialization steps in order to prepare a working directory for use. More details on these are in the sections below, but in most cases it is not necessary to worry about these individual steps.

This command is always safe to run multiple times, to bring the working directory up to date with changes in the configuration. Though subsequent runs may give errors, this command will never delete your existing configuration or state.

If no arguments are given, the configuration in the current working directory is initialized. It is recommended to run Terraform with the current working directory set to the root directory of the configuration, and omit the DIR argument.

![Alt text](../images/terraform_init.png?raw=true)

```
terraform init
```

## terraform plan

The terraform plan command is used to create an execution plan. Terraform performs a refresh, unless explicitly disabled, and then determines what actions are necessary to achieve the desired state specified in the configuration files.

This command is a convenient way to check whether the execution plan for a set of changes matches your expectations without making any changes to real resources or to the state. For example, terraform plan might be run before committing a change to version control, to create confidence that it will behave as expected.

The optional -out argument can be used to save the generated plan to a file for later execution with terraform apply, which can be useful when running Terraform in automation.

# terraform apply

![Alt text](../images/terraform_apply_1.png?raw=true)

![Alt text](../images/terraform_apply_2.png?raw=true)

![Alt text](../images/terraform_apply_3.png?raw=true)

## Verify lambda function is functional

Now, we should be able to invoke the lambda function via awscli
![Alt text](../images/lambda_invoke_via_awscli.png?raw=true)

![Alt text](../images/check_output.png?raw=true)


## Configuring API Gateway

Create a new file api_gateway.tf in the same directory as our lambda.tf from the previous step. 
![Alt text](../images/api_gateway.png?raw=true)

First, configure the root "REST API" object, as follows:

```
resource "aws_api_gateway_rest_api" "example" {
  name        = "ServerlessExample"
  description = "Terraform Serverless Application Example"
}
```
All incoming requests to API Gateway must match with a configured resource and method in order to be handled. Append the following to the lambda.tf file to define a single proxy resource:
```
 resource "aws_api_gateway_resource" "proxy" {
   rest_api_id = aws_api_gateway_rest_api.example.id
   parent_id   = aws_api_gateway_rest_api.example.root_resource_id
   path_part   = "{proxy+}"
}

resource "aws_api_gateway_method" "proxy" {
   rest_api_id   = aws_api_gateway_rest_api.example.id
   resource_id   = aws_api_gateway_resource.proxy.id
   http_method   = "ANY"
   authorization = "NONE"
 }
```

The special path_part value "{proxy+}" activates proxy behavior, which means that this resource will match any request path. Similarly, the aws_api_gateway_method block uses a http_method of "ANY", which allows any request method to be used. Taken together, this means that all incoming requests will match this resource.

Each method on an API gateway resource has an integration which specifies where incoming requests are routed. Add the following configuration to specify that requests to this method should be sent to the Lambda function defined earlier:

```
resource "aws_api_gateway_integration" "lambda" {
   rest_api_id = aws_api_gateway_rest_api.example.id
   resource_id = aws_api_gateway_method.proxy.resource_id
   http_method = aws_api_gateway_method.proxy.http_method

   integration_http_method = "POST"
   type                    = "AWS_PROXY"
   uri                     = aws_lambda_function.example.invoke_arn
 }
```
The AWS_PROXY integration type causes API gateway to call into the API of another AWS service. In this case, it will call the AWS Lambda API to create an "invocation" of the Lambda function.

Unfortunately the proxy resource cannot match an empty path at the root of the API. To handle that, a similar configuration must be applied to the root resource that is built in to the REST API object:

```
 resource "aws_api_gateway_method" "proxy_root" {
   rest_api_id   = aws_api_gateway_rest_api.example.id
   resource_id   = aws_api_gateway_rest_api.example.root_resource_id
   http_method   = "ANY"
   authorization = "NONE"
 }

 resource "aws_api_gateway_integration" "lambda_root" {
   rest_api_id = aws_api_gateway_rest_api.example.id
   resource_id = aws_api_gateway_method.proxy_root.resource_id
   http_method = aws_api_gateway_method.proxy_root.http_method

   integration_http_method = "POST"
   type                    = "AWS_PROXY"
   uri                     = aws_lambda_function.example.invoke_arn
 }
```

Finally, you need to create an API Gateway "deployment" in order to activate the configuration and expose the API at a URL that can be used for testing:
```
resource "aws_api_gateway_deployment" "example" {
   depends_on = [
     aws_api_gateway_integration.lambda,
     aws_api_gateway_integration.lambda_root,
   ]

   rest_api_id = aws_api_gateway_rest_api.example.id
   stage_name  = "test"
 }
```

With all of the above configuration changes in place, run terraform apply again to create these new objects:

```
terraform apply
```
After the creation steps are complete, the new objects will be visible in the https://console.aws.amazon.com/apigateway/home?region=us-east-1.

# Allowing API Gateway to Access Lambda

By default any two AWS services have no access to one another, until access is explicitly granted. For Lambda functions, access is granted using the aws_lambda_permission resource, which should be added to the lambda.tf file created in an earlier step:

```
 resource "aws_lambda_permission" "apigw" {
   statement_id  = "AllowAPIGatewayInvoke"
   action        = "lambda:InvokeFunction"
   function_name = aws_lambda_function.example.function_name
   principal     = "apigateway.amazonaws.com"

   # The "/*/*" portion grants access from any method on any resource
   # within the API Gateway REST API.
   source_arn = "${aws_api_gateway_rest_api.example.execution_arn}/*/*"
 }
```
In order to test the created API you will need to access its test URL. To make this easier to access, add the following output to api_gateway.tf:
```
output "base_url" {
  value = aws_api_gateway_deployment.example.invoke_url
}
```

```
terraform apply
```

