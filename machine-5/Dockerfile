FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install services for Machine 5
RUN apt-get update && apt-get install -y \
    supervisor \
    apache2 \
    php \
    libapache2-mod-php \
    postgresql \
    openssh-server \
    openjdk-11-jdk \
    redis-server \
    wget \
    curl \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Jenkins 2.426.3 LTS (Vulnerable to CVE-2024-23897)
RUN mkdir -p /opt/jenkins && \
    wget https://get.jenkins.io/war-stable/2.426.3/jenkins.war -O /opt/jenkins/jenkins.war

# Fix postgres permissions
RUN mkdir -p /var/run/postgresql && chown postgres:postgres /var/run/postgresql

# Configure SSH
RUN mkdir /var/run/sshd
RUN echo 'root:securepassword' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Configure Laravel on Port 511
RUN sed -i 's/Listen 80/Listen 511/' /etc/apache2/ports.conf
RUN sed -i 's/<VirtualHost \*:80>/<VirtualHost *:511>/' /etc/apache2/sites-available/000-default.conf
WORKDIR /var/www/html
COPY laravel/index.php .

# Supervisor Config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 511 22 8080 5432 6379

ENTRYPOINT ["/entrypoint.sh"]
