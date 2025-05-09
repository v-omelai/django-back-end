#!/bin/bash

cd ..
sudo apt update
sudo apt upgrade
sudo apt install -y python3-venv
sudo apt install -y python3-pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
