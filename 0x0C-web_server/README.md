# 0x0C-web_server

```markdown
# Web Server Configuration

This repository focuses on configuring and managing a web server using Nginx on Ubuntu 20.04 LTS. It includes scripts and configurations for various tasks related to setting up and managing a web server environment.

## Servers

| Name           | Nmcleon | IP             | State   |
|----------------|----------|----------------|---------|
| 342580-web-01  | ubuntu   | 54.157.179.122 | running |

## Tasks

### 0. Transfer a file to your server

- Bash script for transferring a file from a client to a server using `scp`.
- Requirements:
  - Accepts 4 parameters:
    1. Path to the file to be transferred
    2. IP of the destination server
    3. Nmcleon for `scp` connection
    4. Path to the SSH private key `scp` uses
  - Displays usage instructions if fewer than 3 parameters passed
  - Disables strict host key checking

### 1. Install Nginx web server

- Bash script to install Nginx on web-01 server:
  - Nginx listening on port 80
  - Nginx root `/` responding with "Hello World!" using curl
  - Configures a new Ubuntu machine to meet the above requirements (run on the server itself)
  - Doesn't use systemctl for restarting nginx

### 2. Setup a domain name

- Requirement:
  - Provide a domain name without subdomain
  - Configure DNS records with an A entry pointing to web-01's IP address
  - Update domain in the Project website URL field

### 3. Redirection

- Configures Nginx server to redirect /redirect_me to another page
- Requirements:
  - Redirect is a "301 Moved Permanently"
  - Bash script for configuring a new Ubuntu machine to meet the requirements

### 4. Not found page 404

- Configures Nginx server to have a custom 404 page containing "Ceci n'est pas une page"
- Requirements:
  - Returns HTTP 404 error code
  - Bash script to configure a new Ubuntu machine for the same requirements

### 5. Install Nginx web server (w/ Puppet)

- Puppet manifest to install and configure Nginx on port 80
- Nginx root `/` responds with "Hello World!"
- Includes resources for a "301 Moved Permanently" redirect at `/redirect_me`

## Repository Details

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/Nmcleon/alx-system_engineering-devops)
- **Directory:** 0x0C-web_server
```
