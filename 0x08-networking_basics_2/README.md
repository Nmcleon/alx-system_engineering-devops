# 0x08-networking_basics_2
# Networking Basics 2

This repository contains Bash scripts for configuring and managing network settings on an Ubuntu server. Below are the details and usage instructions for each script.

## 0. Change Your Home IP (mandatory)

This Bash script configures an Ubuntu server to meet the following requirements:

- `localhost` resolves to `127.0.0.2`.
- `facebook.com` resolves to `8.8.8.8`.

**Usage:**

```bash
sylvain@ubuntu$ ping localhost
# Verify localhost resolves to 127.0.0.1

sylvain@ubuntu$ ping facebook.com
# Verify facebook.com resolves to the original IP (e.g., 157.240.11.35)

sylvain@ubuntu$ sudo ./0-change_your_home_IP
# Run the script to change the IP configurations

sylvain@ubuntu$ ping localhost
# Verify localhost now resolves to 127.0.0.2

sylvain@ubuntu$ ping facebook.com
# Verify facebook.com now resolves to 8.8.8.8
```

**Note:** Remember to revert the changes to `localhost` after using this script if you continue using the machine regularly.

Repository Path: `alx-system_engineering-devops/0x08-networking_basics_2/0-change_your_home_IP`

## 1. Show Attached IPs (mandatory)

This Bash script displays all active IPv4 IPs on the machine it's executed on.

**Usage:**

```bash
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
# Run the script to display active IPv4 IPs on the machine
# Example output:
# 10.0.2.15$
# 127.0.0.1$
```

Repository Path: `alx-system_engineering-devops/0x08-networking_basics_2/1-show_attached_IPs`

## 2. Port Listening on localhost (advanced)

This Bash script listens on port 98 on localhost, allowing you to establish a connection for debugging or testing purposes.

**Usage:**

Terminal 0 (Start the script to listen):

```bash
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
# Start the script to listen on port 98
```

Terminal 1 (Connect and send data):

```bash
sylvain@ubuntu$ telnet localhost 98
# Connect to localhost on port 98 using telnet and send text
# Example input:
# Hello world
# test
```

Terminal 0 (Receive the text on the other side):

```bash
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
# Receive the text sent from Terminal 1
```

**Note:** This script can be used for debugging socket connection issues or testing network configurations.
