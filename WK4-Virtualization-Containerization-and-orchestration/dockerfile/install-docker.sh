#!/bin/bash
set -e

# Please only execute it in our vagrant machine. For Ubuntu Desktop, please google installation guides
echo Installing docker ...
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker vagrant
sudo newgrp docker 
