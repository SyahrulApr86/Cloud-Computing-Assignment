#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git bridge-utils
sudo apt install -y containerd
sudo systemctl enable containerd
sudo systemctl start containerd
git clone https://github.com/openfaas/faasd --depth=1
cd faasd
sudo ./hack/install.sh

sudo cat /var/lib/faasd/secrets/basic-auth-password
