#!/bin/bash

# Initialize MySQL
if [ ! -d "/var/lib/mysql/mysql" ]; then
    mysqld --initialize-insecure --user=mysql
fi

# Start MySQL temporarily
mysqld_safe &
while ! mysqladmin ping --silent; do
    sleep 1
done

mysql -e "CREATE USER IF NOT EXISTS 'wordpress'@'localhost' IDENTIFIED BY 'wordpresspassword';"
mysql -e "CREATE DATABASE IF NOT EXISTS wordpress;"
mysql -e "GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"

mysqladmin shutdown

# Start Supervisor
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
