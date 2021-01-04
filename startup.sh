#!/bin/bash
sudo apt update
sudo apt-get install python3-venv -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
#pip3 install flask-wtf
pytest

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service

python3 create.py
python3 app.py
