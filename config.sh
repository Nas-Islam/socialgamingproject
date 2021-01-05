#!/bin/bash
sudo apt update
sudo apt-get install python3-venv


# Test Phase
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# pytest goes here
pytest tests/test_app.py --cov=application

# Make the installation directory
sudo cp -r application /opt/sgproject/application
sudo cp -r tests /opt/sgproject/tests
sudo cp -r app.py /opt/sgproject/app.py
sudo cp -r create.py /opt/sgproject/create.py
sudo cp -r requirements.txt /opt/sgproject/requirements.txt
sudo cp -r startup.sh /opt/sgproject/startup.sh

# Give jenkins user permissions for the installation directory
sudo chown -R jenkins /opt/sgproject


sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service

