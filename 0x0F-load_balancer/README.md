# 0x0F-load_balancer

### Task 0: Double the number of webservers
- **Objective**: Configure `web-02` to mirror the setup of `web-01` and ensure Nginx responds with a custom header.
- **Solution**: Create a Bash script (`0-custom_http_response_header`) that configures a new Ubuntu machine to have Nginx responses with a custom header.

### Task 1: Install your load balancer
- **Objective**: Install and configure HAProxy on `lb-01` to distribute traffic between `web-01` and `web-02` using a round-robin algorithm.
- **Solution**: Write a Bash script (`1-install_load_balancer`) that configures a new Ubuntu machine to install and set up HAProxy to meet the specified requirements.

### Task 2: Add a custom HTTP header with Puppet
- **Objective**: Use Puppet to automate the configuration of a custom HTTP header in the Nginx response.
- **Solution**: Create a Puppet script (`2-puppet_custom_http_response_header.pp`) to configure a new Ubuntu machine to ensure Nginx responses contain the custom HTTP header.

Each task revolves around automating the setup and configuration of web servers and load balancers while ensuring that Nginx responses include the specified custom HTTP header.
