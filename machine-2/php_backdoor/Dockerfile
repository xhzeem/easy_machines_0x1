FROM php:8.1-apache
# Simulating the PHP 8.1.0-dev backdoor logic in a way that works on any PHP version for the lab
# The real backdoor was in the PHP source, but here we can just add a small snippet to index.php
COPY index.php /var/www/html/
COPY assets/ /var/www/html/assets/
EXPOSE 80
