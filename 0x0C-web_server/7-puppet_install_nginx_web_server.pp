# manifst using puppet to automate

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path => '/etc/nginx/sites_enabled/default'
  after => 'rewrite ^/redirect_me https://www.github.com/Nmcleon permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
