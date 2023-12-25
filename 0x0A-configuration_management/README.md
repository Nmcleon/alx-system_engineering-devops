# 0x0A-configuration_management

```markdown
# Puppet Configuration Management

This repository contains Puppet manifests for various tasks related to configuration management using Puppet. All files are intended for execution on Ubuntu 20.04 LTS and comply with specific requirements outlined below.

## Requirements

### General

- All files should be interpreted on Ubuntu 20.04 LTS.
- Each file should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- Puppet manifests must adhere to the puppet-lint version 2.1.1 without any errors.
- Puppet manifests should run without any errors.
- The first line of Puppet manifests must be a comment explaining the purpose of the manifest.
- Puppet manifest files must have the extension .pp.

### Versioning

- The Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Installation Instructions

#### Install Puppet
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

#### Puppet 5 Docs
Refer to [Puppet 5 Documentation](https://puppet.com/docs/puppet/5.5/index.html) for additional details.

#### Install puppet-lint
```bash
$ gem install puppet-lint
```

## Tasks

### 0. Create a file

#### Requirements

- Create a file in /tmp with the following specifications:
  - File path: /tmp/school
  - File permission: 0744
  - File owner: www-data
  - File group: www-data
  - File content: "I love Puppet"

#### Example
```bash
$ puppet apply 0-create_a_file.pp
```

### 1. Install a package

#### Requirements

- Install Flask from pip3 with the version being 2.1.0.

#### Example
```bash
$ puppet apply 1-install_a_package.pp
```

### 2. Execute a command

#### Requirements

- Use the exec Puppet resource to kill a process named "killmenow" using `pkill`.

#### Example
```bash
$ puppet apply 2-execute_a_command.pp
```

## Repository Details

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/Nmcleon/alx-system_engineering-devops)
- **Directory:** 0x0A-configuration_management
```
