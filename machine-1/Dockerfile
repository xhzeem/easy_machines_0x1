FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install all services for Machine 1
RUN apt-get update && apt-get install -y \
    supervisor \
    openssh-server \
    vsftpd \
    redis-server \
    nginx \
    python3 \
    python3-pip \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Configure SSH
RUN mkdir /var/run/sshd
RUN echo 'root:password123' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Configure FTP
RUN mkdir -p /var/run/vsftpd/empty
COPY vsftpd.conf /etc/vsftpd.conf
RUN mkdir -p /srv/ftp/anonymous && chown ftp:ftp /srv/ftp/anonymous
RUN echo "FLAG{ANON_FTP_L0G1N}" > /srv/ftp/anonymous/flag.txt

# Configure Nginx (Port 115 inside, but mapped to host)
# Default nginx is on 80. We'll change it to 115 inside to avoid conflict with web app if we wanted, 
# but we can just map them in docker-compose.
# Let's keep internal ports standard where possible.
RUN sed -i 's/listen 80 default_server;/listen 115 default_server;/' /etc/nginx/sites-available/default

# Web App Setup (Python)
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .

# Supervisor Config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80 22 21 6379 115

CMD ["/usr/bin/supervisord"]
