#!/bin/bash
# Use this as the user data when launching a EC2 instance
APP_FOLDER=/home/ubuntu/flask-test-2
NGINX_CONF=/etc/nginx/sites-enabled/flaskapp.conf
HOST=$(curl checkip.amazonaws.com)
echo export HOST=$(curl checkip.amazonaws.com) >> /etc/profile

su ubuntu
git clone https://github.com/julioct99/flask-test-2.git /home/ubuntu/flask-test-2

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install python3-pip -y
pip3 install -r $APP_FOLDER/requirements.txt 
sudo apt install gunicorn -y
sudo apt-get install nginx -y
chmod +x $APP_FOLDER/*.sh

sudo cp $APP_FOLDER/nginx/flaskapp.conf $NGINX_CONF
sudo sed -i "s/__HOST/${HOST}/g" $NGINX_CONF
sudo service nginx restart
cd $APP_FOLDER && ./start.sh