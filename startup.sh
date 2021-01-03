#!/bin/bash 
cd /opt/socialgamingproject
sudo mkdir /socialgamingproject
sudo chown -R jenkins /socialgamingproject
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
