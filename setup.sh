#!/bin/bash
APP_FOLDER=~/flask-test-2
NGINX_CONF=/etc/nginx/sites-enabled/flaskapp.conf

git clone https://github.com/julioct99/flask-test-2.git

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install python3-pip -y
pip3 install -r $APP_FOLDER/requirements.txt 
chmod +x $APP_FOLDER/*.sh

sudo apt install gunicorn -y
sudo apt-get install nginx -y

sudo cp $APP_FOLDER/nginx/flaskapp.conf $NGINX_CONF
sudo sed -i "s/__HOST/${HOST}/g" $NGINX_CONF
sudo service nginx restart
cd $APP_FOLDER && ./start.sh