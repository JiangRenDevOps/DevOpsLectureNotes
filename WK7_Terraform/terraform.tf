terraform {
  backend "s3" {
    encrypt = true
    bucket = "terraform-remote-state-storage-s3-yu-wang"
    region = "us-east-1"
    key = "./terraform.tfstate"
    profile = "goggle"

    # Replace this with your DynamoDB table name!
    dynamodb_table = "terraform-state-lock-dynamodb"
  }
}