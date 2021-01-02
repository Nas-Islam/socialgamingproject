#!/bin/bash 

sudo apt update
sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

sudo mkdir /opt/socialgamingproject
sudo chown -R jenkins /opt/socialgamingproject

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service