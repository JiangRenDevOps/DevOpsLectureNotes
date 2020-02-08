module "key_pair" {
  source = "terraform-aws-modules/key-pair/aws"

  key_name   = "SSH key imported from laptop for app"
  public_key = "${data.local_file.public_key.content}"

}

data "local_file" "public_key" {
    filename = "/root/.ssh/id_rsa.pub"
}
