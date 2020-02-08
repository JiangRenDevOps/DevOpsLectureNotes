# Description

This is the terraform project to create JRCMS infrastructure.

# Folder Structure

## 1.s3-state

This terraform project creates a S3 bucket to store terraform states.

## 2.global

Global AWS resources that should be created only once-off.
- vpc
- s3 to store Terraform state
