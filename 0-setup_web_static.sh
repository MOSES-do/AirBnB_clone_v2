#!/usr/bin/env bash
# Set up web servers for deployment of web_static

# Update the server.
sudo apt-get update

sudo apt-get -y install nginx

sudo ufw allow 'OpenSSH'
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 'Nginx HTTPS'

sudo mkdir -p /data/web_static/releases/test/

sudo mkdir -p /data/web_static/shared/

sudo touch /data/web_static/releases/test/index.html

sudo bash -c 'echo "<html>
  <head>
  </head>
  </body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Serve content of /data/web_static/current/ to hbnb_static
# using alias.
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx after configuration.
sudo service nginx restart
