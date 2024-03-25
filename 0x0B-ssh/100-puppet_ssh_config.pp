# Puppet to make changes to our configuration file
file_line { 'Set up SSH client configuration':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => [
    '    PasswordAuthentication no',
    '    IdentityFile ~/.ssh/school'
  ],
}
