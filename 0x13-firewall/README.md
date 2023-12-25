# 0x13-firewall
(reminder .. check 100 on web-01... run it later)

In the first task, you'll be setting up the `ufw` firewall to block all incoming traffic except for specific TCP ports (22, 80, 443). This can be achieved by configuring `ufw` with specific rules.

### Task 0: Block all incoming traffic but
- **Objective**: Configure `ufw` on `web-01` to block all incoming traffic except for ports 22, 80, and 443.
- **Solution**: Create a Bash script (`0-block_all_incoming_traffic_but`) that contains `ufw` commands to set up the firewall rules allowing only SSH (port 22), HTTP (port 80), and HTTPS (port 443) traffic. Share the commands used in the answer file.

For the second task, it involves configuring `web-01`'s firewall to forward traffic from port 8080 to port 80. This process is accomplished by altering the firewall configuration to redirect incoming traffic from one port to another.

### Task 1: Port forwarding
- **Objective**: Configure `web-01`'s firewall to redirect incoming traffic from port 8080/TCP to port 80/TCP.
- **Solution**: Your answer file should include the modified `ufw` configuration file that enables the port forwarding from 8080 to 80. This setup ensures that requests to `web-01` on port 8080 are redirected to port 80.

Each task revolves around using `ufw` to manage the firewall rules, allowing or redirecting specific traffic while blocking all other incoming connections except for those specified. This helps in securing the server by only allowing necessary traffic.
