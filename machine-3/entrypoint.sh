#!/bin/bash

# Initialize MongoDB
mkdir -p /data/db
chown -R mongodb:mongodb /data/db

# Start Supervisor
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
