#!/bin/bash
sudo apt update
sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install flask-wtf

python3 create.py
python3 app.py
