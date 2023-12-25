# 0x0E-web_stack_debugging_1

### Task 0: Nginx likes port 80
- Diagnosis: The Nginx installation is not listening on port 80.
- Resolution: Write a Bash script to configure Nginx to listen on port 80.

```bash
#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y install nginx
sudo sed -i 's/80 default_server;/80;/g' /etc/nginx/sites-available/default
sudo service nginx restart
```

### Task 1: Make it sweet and short
- Diagnosis: Service (init) is showing that Nginx is not running.
- Resolution: Create a compact Bash script (5 lines or less) to ensure Nginx is running and listening on port 80.

```bash
#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y install nginx
echo "listen 80;" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
```

The script ensures that Nginx is installed, configures it to listen on port 80, and restarts the Nginx service to apply the changes.
