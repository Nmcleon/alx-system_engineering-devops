# 0x10-https_ssl

### Task 0: World wide web
- **Objective**: Configure the domain zone to point specific subdomains (`www`, `lb-01`, `web-01`, `web-02`) to their respective IP addresses and create a Bash script that displays information about subdomains.
- **Solution**: Write a Bash script (`0-world_wide_web`) that accepts domain and subdomain parameters and provides information about the specified subdomain or displays information for predefined subdomains if no subdomain is specified.

### Task 1: HAProxy SSL termination
- **Objective**: Configure HAProxy to terminate SSL, serve encrypted traffic for the `www` subdomain, and return the root of the web server with a specific content.
- **Solution**: Create an HAProxy configuration file (`1-haproxy_ssl_termination`) that listens on TCP 443, accepts SSL traffic, and serves encrypted traffic for the `www` subdomain.

### Task 2: No loophole in your website traffic
- **Objective**: Configure HAProxy to automatically redirect HTTP traffic to HTTPS transparently without impacting the user experience.
- **Solution**: Create an HAProxy configuration file (`100-redirect_http_to_https`) that returns a 301 for HTTP traffic, redirecting it to HTTPS.

Each task involves setting up and configuring HAProxy to manage domain zones, SSL termination, and enforce HTTPS traffic, ensuring secure and encrypted communication for specific subdomains.
