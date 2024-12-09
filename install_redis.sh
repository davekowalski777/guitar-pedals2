#!/bin/bash

# Download Redis
curl -O http://download.redis.io/redis-stable.tar.gz

# Unpack tarball
tar xvzf redis-stable.tar.gz

# Build Redis
cd redis-stable
make

# Install Redis binaries
sudo cp src/redis-server /usr/local/bin/
sudo cp src/redis-cli /usr/local/bin/

# Create Redis configuration directory
sudo mkdir -p /etc/redis
sudo cp redis.conf /etc/redis/

# Start Redis server
redis-server /etc/redis/redis.conf &

echo "Redis installation complete!"
