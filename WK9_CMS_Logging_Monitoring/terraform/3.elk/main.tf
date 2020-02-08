provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {}
}

data "terraform_remote_state" "s3_state" {
    backend = "local"
    config = {
        path = "../1.s3-state/terraform.tfstate"
    }
}

data "terraform_remote_state" "global_state" {
    backend = "s3"
    config = {
        bucket = "${data.terraform_remote_state.s3_state.outputs.bucket_raw}"
        key    = "2.global/terraform.tfstate"
        region = "${data.terraform_remote_state.s3_state.outputs.region_raw}"
    }
}
