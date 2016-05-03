#!/bin/bash

set -x
upro=yum
setup_folder="./venv-setup"
ot=$(cat /etc/issue | grep Ubuntu)
if [ ! -z "$ot" ] 
  then
     Ubuntu=True
     upro="apt-get"   
     $ sudo $upro install software-properties-common -y
     $ sudo $upro update
     $ sudo apt-add-repository ppa:ansible/ansible-1.9 -y
  else
    sudo $upro install libselinux-python -y
fi

sudo $upro install python-pip -y
sudo pip install --upgrade pip
$ sudo $upro install ansible -y


sudo $upro install ansible -y
sudo pip install -r ${setup_folder}/requirments.txt
cp ${setup_folder}/aws-key.pem ~/.ssh/  &&  chmod 600 ~/.ssh/aws-key.pem
cp ${setup_folder}/ssh-config.txt ~/.ssh/config && chmod 600  ~/.ssh/config

echo  run source ${setup_folder}/.bashrc to complete the setup





