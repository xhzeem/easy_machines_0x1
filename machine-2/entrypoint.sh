#!/bin/bash

# Start Supervisor directly - services are initialized in supervisor
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
