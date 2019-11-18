# Description

This is to demo how to use SSH.

# Pre-requisite

A Linux box or a Macbook

# Task 1: Generate a ssh key pair and send your public key to the channel
Command:
```
ssh-keygen
cat ~/.ssh/id_rsa.pub
```
Example:
```
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/davis/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/davis/.ssh/id_rsa.
Your public key has been saved in /home/davis/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:vNwb6VCRqFtoUWSW28nNqJZUEOxgxLv5zg6wYyUYYag davis@dliu-atlassian
The key's randomart image is:
+---[RSA 3072]----+
| .o  o.oB+       |
|.. .  ++o...     |
|. .  ..+.=o=     |
|E  o  .=+ =.o    |
|  . o =+So.      |
|     *o+++ .     |
|    + oo+ +      |
|   . . o.o o     |
|       o+ o      |
+----[SHA256]-----+
$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCwc51cMxwdNOMVMCgbUqpPvEF+5mkChB51AmYgVIJqvgPEgp0w10lWdJPI6rphNbByVQYLCOWSaEpZ+pbmKYkHxGeJBr8NLbny2bgSMyX05/BaxBGJpVfNx8SO2HkGuq7FOk8W7dFzNiPqD0HQIEJLSMcyPjZtYHarqWDz8Xe7Y0IIA5U6Q5TJzF/CQEFsY4x+5bWqTDuQjtKNfPLw6yU5g3HtdJb7EIFEGpLQTajuioOXTcop87CjfOGYH8YW94N1nCulVGW3pe+Qx1lab7lJ/r8i95JxN64Al9i8sHQSejNw8n01rSzfLVrf9DfszqGw+mv270eDMaajFgfMlcaCFYSWESheguhxv5VNBpW/VBma8Mt1e/yYbMW1bGbuFSK1o+CpM9wv1X1tg9MbJ0YS8DksqdKadtb8AZy8GFDw50xEqS7TRTjeDxkIGpSGJKqr6w9OMJ2hVsCHa4UPkkan8YJaIwCLOGW+/xH5jU4fhoZIhgvuHu1tn0SalCFnm8c=
```

Please send your public key to the wechat channel. Your teacher will add your public key to the server.

# Task 2: SSH to a remote server
Command:
```
ssh ec2-user@xxx
touch "Your Name"
```
Example:
```
ssh ec2-user@xxx
touch "Davis"
```

# Task 3: Download a local file to the server
```
scp ec2-user@xxx:test.html .
```
You should be able to open the test.html from your laptop.
