#!/bin/bash
cd ~/workspace/
sudo apt-get install python3
sudo pip install virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate

sudo easy_install Flask
