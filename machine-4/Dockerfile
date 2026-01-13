FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install services for Machine 4
RUN apt-get update && apt-get install -y \
    supervisor \
    apache2 \
    php \
    libapache2-mod-php \
    php-mysql \
    mysql-server \
    openssh-server \
    nginx \
    wget \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Grafana 8.3.0 (Vulnerable to CVE-2021-43798)
RUN ARCH=$(dpkg --print-architecture) && \
    wget https://dl.grafana.com/oss/release/grafana_8.3.0_${ARCH}.deb && \
    dpkg -i grafana_8.3.0_${ARCH}.deb && \
    rm grafana_8.3.0_${ARCH}.deb

# Configure SSH
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Configure WordPress on Port 411
RUN sed -i 's/Listen 80/Listen 411/' /etc/apache2/ports.conf
RUN sed -i 's/<VirtualHost \*:80>/<VirtualHost *:411>/' /etc/apache2/sites-available/000-default.conf
WORKDIR /var/www/html
RUN wget https://wordpress.org/latest.zip && unzip latest.zip && mv wordpress/* . && rm -rf wordpress latest.zip
COPY wp-config.php .
RUN wget https://downloads.wordpress.org/plugin/wp-file-manager.6.0.zip -P /tmp/ && \
    unzip /tmp/wp-file-manager.6.0.zip -d /var/www/html/wp-content/plugins/ && \
    rm /tmp/wp-file-manager.6.0.zip
RUN chown -R www-data:www-data /var/www/html

# Configure Nginx (Port 415)
RUN sed -i 's/listen 80 default_server;/listen 415 default_server;/' /etc/nginx/sites-available/default

# Supervisor Config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 411 22 3306 3000 415

ENTRYPOINT ["/entrypoint.sh"]
