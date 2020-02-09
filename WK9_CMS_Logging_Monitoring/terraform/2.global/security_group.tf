module "web_server_sg" {
  source = "terraform-aws-modules/security-group/aws//modules/http-80"

  name        = "web-server"
  description = "Security group for web-server with HTTP ports open within VPC"
  vpc_id      = "${module.vpc.vpc_id}"

  ingress_cidr_blocks = ["0.0.0.0/0"]

  tags = {
    Terraform   = "true"
    Name        = "Allow Web Server traffic"
    Project     = "jrcms"
  }
}

module "ssh_sg" {
  source = "terraform-aws-modules/security-group/aws//modules/ssh"

  name        = "ssh"
  description = "Security group for ssh open within VPC"
  vpc_id      = "${module.vpc.vpc_id}"

  ingress_cidr_blocks = ["0.0.0.0/0"]

  tags = {
    Terraform   = "true"
    Name        = "Allow Web SSH traffic"
    Project     = "jrcms"
  }
}

resource "aws_security_group" "allow_all" {
  name        = "allow_all"
  description = "Allow all traffic - Test Only"
  vpc_id      = "${module.vpc.vpc_id}"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
  tags = {
    Terraform   = "true"
    Name        = "Allow all traffic for test purpose"
    Project     = "jrcms"
  }
}

output "web_server_sg_id" {
  value = "${module.web_server_sg.this_security_group_id}"
}
output "ssh_sg_id" {
  value = "${module.ssh_sg.this_security_group_id}"
}
output "all_sg_id" {
  value = "${aws_security_group.allow_all.id}"
}
