FROM php:7.4-apache

# Install dependencies for a "full app" feel
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

# Mimic a Laravel structure
COPY . .

# Enable rewrite
RUN a2enmod rewrite
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

EXPOSE 80
