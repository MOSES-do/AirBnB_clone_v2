#!/usr/bin/env bash
# Setting up web servers file/folder structure for deployment of web static

# verifying installation of program "nginx"  else install
prog_name="nginx"

if command -v "$prog_name" >/dev/null; then
       :
else
       sudo apt update
       sudo apt-get -y install nginx
       sudo sed -i 's/80/80/g' /etc/nginx/sites-enabled/default

       echo "Hello World!" > /var/www/html/index.html

       sudo service nginx restart
fi

# create folder/file structure if it doesn't already exist
root_folder="/data"
web_static="$root_folder/web_static"
releases="$web_static/releases"
shared="$web_static/shared"
test_dir="$releases/test"
test_file="index.html"


list_dir=("$root_folder" "$web_static" "$releases" "$shared" "$test_dir")

for directory in "${list_dir[@]}"; do
        if [ ! -d "$directory" ]; then
                sudo mkdir -p "$directory"
        else
                :
        fi
done

if [ -d "/data/web_static/releases/test/" ]; then
        if [ ! -f "$test_file" ]; then
                touch "$test_dir/$test_file"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "$test_dir/$test_file"
        fi
fi


# set ownership tp current user/group
sudo chown -R "$USER:$USER" /data
sudo chmod 755 /data/web_static/releases/test/index.html

# check if symbolic link exists, if yes, delete and recreate it
sym_link="/data/web_static/current"
target_path="/data/web_static/releases/test"
if [ -L "$sym_link" ]; then
        sudo rm "$sym_link"
fi
sudo ln -s "$target_path" "$sym_link"

nginx_conf="/etc/nginx/sites-available/default"
new_root="root /data/web_static/current/;"
my_new_server="server_name aceme.tech www.aceme.tech;"
# replacements using sed -i
sudo sed -i "s#server_name _;#$my_new_server#" "$nginx_conf"
sudo sed -i "s#root /var/www/html;#$new_root#" "$nginx_conf"


# recreate symlink for sites-enabled to update using sites-available
sym_link1="/etc/nginx/sites-enabled/default"
target_path1="/etc/nginx/sites-available/default"
if [ -L "$sym_link1" ]; then
        sudo rm "$sym_link1"
fi
sudo ln -s "$target_path1" "$sym_link1"

redirect_path="/hbnb_static"
path="alias /data/web_static/current"
sudo sed -i "/add_header X-Served-By \$HOSTNAME;/a\\
\\tlocation $redirect_path {\\
\\t\\t$path;\\
\\t}\\
" "$nginx_conf"

sudo nginx -t

# If the configuration test is successful, reload Nginx to apply the changes
sudo service nginx restart
