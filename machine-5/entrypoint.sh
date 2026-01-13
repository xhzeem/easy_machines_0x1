#!/bin/bash

# Initialize Postgres if not initialized
if [ ! -d "/var/lib/postgresql/14/main" ]; then
    sudo -u postgres /usr/lib/postgresql/14/bin/initdb -D /var/lib/postgresql/14/main
fi

# Start Supervisor
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
