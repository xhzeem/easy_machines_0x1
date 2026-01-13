FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install services for Machine 3
RUN apt-get update && apt-get install -y \
    supervisor \
    curl \
    telnetd \
    memcached \
    lighttpd \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install MongoDB from official repo
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | \
    gpg --dearmor -o /usr/share/keyrings/mongodb-server-6.0.gpg && \
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | \
    tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && apt-get install -y mongodb-org && \
    rm -rf /var/lib/apt/lists/*

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Configure Telnet
RUN mkdir -p /var/run/telnetd
RUN useradd -m admin && echo "admin:admin" | chpasswd

# Web App Setup (Node)
WORKDIR /app
COPY node_vuln_files/package.json .
RUN npm install
COPY node_vuln_files/server.js .

# Configure Lighttpd (Port 315)
RUN sed -i 's/server.port                 = 80/server.port                 = 315/' /etc/lighttpd/lighttpd.conf

# Supervisor Config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 3000 23 27017 11211 315

ENTRYPOINT ["/entrypoint.sh"]
