#!/usr/bin/env bash
# Install and configure HAproxy lb-01 server.
sudo apt-get -y update
apt-get -y install haproxy

# edit config file
server_config=\
"
frontend  besthor_frontend
        bind *:80
        mode http
        default_backend nmcleon_backend
backend nmcleon_backend
        balance roundrobin
        server 342580-web-01 54.160.126.3 check
        server 342580-web-02 100.26.234.54 check
"
echo "$server_config" | sudo tee -a /etc/haproxy/haproxy.cfg

echo "ENABLED=1" | sudo tee -a /etc/default/haproxy

# Test HAproxy configuration file
sudo haproxy -c -f /etc/haproxy/haproxy.cfg

# Restart Nginx service
sudo service haproxy restart
