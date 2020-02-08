module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "s3-terraform-state-storage-${random_string.random.result}"

  versioning = {
    enabled = true
  }

  tags = {
    Name        = "Terraform State Storage"
    Project     = "jrcms"
  }

}

resource "random_string" "random" {
  length = 5
  special = false
  upper = false
}

output "bucket_raw" {
  value = "${module.s3_bucket.this_s3_bucket_id}"
}

output "region_raw" {
  value = "${module.s3_bucket.this_s3_bucket_region}"
}

output "bucket_parameter" {
  value = "bucket=\"${module.s3_bucket.this_s3_bucket_id}\""
}

output "region_parameter" {
  value = "region=\"${module.s3_bucket.this_s3_bucket_region}\""
}
