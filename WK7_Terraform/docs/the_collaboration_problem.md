# Intro
When your are building infrastructure with terraform config, a state file, called terraform.tfstat, gets generated locally in the local directory. This state file contains information about the infrastructure and configuration that terraform is managing. 

## Whats in the state file?
The state file contains information about what real resources exist for each object defined in the terraform config files. For example, if you have a DNS zone resource created in your terraform config, then the state file contains info about the actual resource that was created on AWS.

lets check out what is our terraform.tfstate

```
less terraform.tfstate
```

## The problem
If you’re using Terraform for a personal project, storing state in a local terraform.tfstate file works just fine. But if you want to use Terraform as a team on a real product, you run into several problems:

__Shared storage for state files__: To be able to use Terraform to update your infrastructure, each of your team members needs access to the same Terraform state files. That means you need to store those files in a shared location.

__Locking state files__: As soon as data is shared, you run into a new problem: locking. Without locking, if two team members are running Terraform at the same time, you may run into race conditions as multiple Terraform processes make concurrent updates to the state files, leading to conflicts, data loss, and state file corruption.

__Isolating state files__: When making changes to your infrastructure, it’s a best practice to isolate different environments. For example, when making a change in the staging environment, you want to be sure that you’re not going to accidentally break production. But how can you isolate your changes if all of your infrastructure is defined in the same Terraform state file?

#Solution
When working on a team, it is better to store this state file remotely so that more folks can access it to make changes to the infrastructure.

Terraform, as of v0.9, offers locking remote state management. To get it up and running in AWS create a terraform s3 backend, an s3 bucket and a dynamDB table.


## Build the s3
Let us create the bucket
```
aws s3api create-bucket --bucket=terraform-remote-state-storage-s3-yu-wang --region=us-east-1 --profile goggle
```
result:
```
{
    "Location": "/terraform-remote-state-storage-s3-yu-wang"
}
```
let us create a file called `backend.tf`
```
resource "aws_s3_bucket" "terraform-state-storage-s3-yu-wang" {
  bucket = "terraform-remote-state-storage-s3-yu-wang"

  versioning {
    enabled = true
  }

}
```

Next, you need to create a DynamoDB table to use for locking. DynamoDB is Amazon’s distributed key-value store. It supports strongly-consistent reads and conditional writes, which are all the ingredients you need for a distributed lock system. Moreover, it’s completely managed, so you don’t have any infrastructure to run yourself, and it’s inexpensive, with most Terraform usage easily fitting into the free tier.

add the following to the `backend.tf`
```
resource "aws_dynamodb_table" "dynamodb-terraform-state-lock" {
  name         = "terraform-state-lock-dynamodb"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}
```

and let us add the following to `terraform.tf`
```
terraform {
  backend "s3" {
    encrypt = true
    bucket = "terraform-remote-state-storage-s3-yu-wang"
    region = "us-east-1"
    key = "./terraform.tfstate"
    profile = "goggle"
  }
}
```
run `terraform init`, `terraform plan`, `terraform apply`

Let us add some output to `output.tf`

```
output "s3_bucket_arn" {
  value       = aws_s3_bucket.terraform-state-storage-s3-yu-wang.arn
  description = "The ARN of the S3 bucket"
}
output "dynamodb_table_name" {
  value       = aws_dynamodb_table.dynamodb-terraform-state-lock.name
  description = "The name of the DynamoDB table"
}
```

let us add the following dynamodb_table entry to the backend and rerun
`terraform init`, `terraform plan`, `terraform apply`
```
terraform {
  backend "s3" {
    encrypt = true
    bucket = "terraform-remote-state-storage-s3-yu-wang"
    region = "us-east-1"
    key = "./terraform.tfstate"
    profile = "goggle"
    dynamodb_table = "terraform-state-lock-dynamodb"
  }
}
```


Now, let us check out: https://console.aws.amazon.com/s3/home?region=us-east-1