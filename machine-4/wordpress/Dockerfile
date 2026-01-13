FROM wordpress:latest

# Install vulnerable wp-file-manager plugin (CVE-2020-25213)
RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*
RUN wget https://downloads.wordpress.org/plugin/wp-file-manager.6.0.zip -P /tmp/
RUN unzip /tmp/wp-file-manager.6.0.zip -d /var/www/html/wp-content/plugins/
RUN rm /tmp/wp-file-manager.6.0.zip
RUN chown -R www-data:www-data /var/www/html/wp-content/plugins/wp-file-manager

EXPOSE 80
