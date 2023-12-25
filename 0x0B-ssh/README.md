# 0x0B-ssh

```markdown
# SSH Configuration Management

This repository contains scripts and configurations for managing SSH connections and configurations on Ubuntu 20.04 LTS servers. Below are tasks and their associated requirements.

## General Requirements

- Allowed editors: vi, vim, emacs
- All files must be interpreted on Ubuntu 20.04 LTS
- Files should end with a new line
- All Bash script files must be executable
- The first line of Bash scripts must be `#!/usr/bin/env bash`
- A README.md file at the root is mandatory

## Server Details

| Name          | Nmcleon | IP             | State   |
|---------------|----------|----------------|---------|
| 342580-web-01 | ubuntu   | 54.157.179.122 | running |

## Tasks

### 0. Use a private key

- Write a Bash script using `ssh` to connect to the server using the private key `~/.ssh/school` and user `ubuntu`.

### 1. Create an SSH key pair

- Bash script to generate an RSA key pair:
  - Private key name: school
  - Number of bits: 4096
  - Passphrase protection: betty

### 2. Client configuration file

- Configure SSH client to use `~/.ssh/school` as the private key and refuse authentication using a password.

### 3. Let me in!

- Add the provided SSH public key to the server's `ubuntu` user for access.

### 4. Client configuration file (w/ Puppet)

- Use Puppet to configure the client's SSH configuration file:
  - Use `~/.ssh/school` as the private key
  - Refuse authentication using a password

## Repository Details

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/Nmcleon/alx-system_engineering-devops)
- **Directory:** 0x0B-ssh
```
