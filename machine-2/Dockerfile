FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install services for Machine 2
RUN apt-get update && apt-get install -y \
    supervisor \
    apache2 \
    php \
    libapache2-mod-php \
    mariadb-server \
    postgresql \
    samba \
    && rm -rf /var/lib/apt/lists/*

# Configure Apache for PHP Backdoor on Port 80 (Internal)
RUN sed -i 's/Listen 80/Listen 211/' /etc/apache2/ports.conf
RUN sed -i 's/<VirtualHost \*:80>/<VirtualHost *:211>/' /etc/apache2/sites-available/000-default.conf
WORKDIR /var/www/html
RUN rm -f /var/www/html/index.html
COPY index.php .

# Configure SMB
RUN mkdir -p /share/public && echo "FLAG{SMB_GUEST_ACC3SS}" > /share/public/flag.txt
RUN (echo "[public]"; echo "path = /share/public"; echo "public = yes"; echo "only guest = yes"; echo "writable = yes"; echo "printable = n") >> /etc/samba/smb.conf

# Install sudo for entrypoint
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

# Fix postgres permission issues for local volumes
RUN mkdir -p /var/run/postgresql && chown postgres:postgres /var/run/postgresql

# 5th Service: A separate Apache instance on port 215 simulating a vulnerable one
RUN cp -r /etc/apache2 /etc/apache2-vuln
RUN sed -i 's/Listen 211/Listen 215/' /etc/apache2-vuln/ports.conf
RUN sed -i 's/VirtualHost \*:211/VirtualHost *:215/' /etc/apache2-vuln/sites-available/000-default.conf

# Supervisor Config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 211 3306 445 5432 215

ENTRYPOINT ["/entrypoint.sh"]
