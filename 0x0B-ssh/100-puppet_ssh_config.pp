#!/usr/bin/env bash
# Puppet Manifest.
# Using puppet to make changse in config file

file {'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH CLIENT CONFIGURATION
	host*
	IdentifyFile ~/.ssh/school
	PasswordAuthentification no
	"
}
