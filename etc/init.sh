sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf ./nginx.conf /etc/nginx/sites-enabled/my.conf
sudo service nginx restart