# ansiblePower
My test  Project

#########################################
###   Configuration vagrant dev env   ###
#########################################
1) run vagrant env
Tools -> Vagrant -> up

2) configure sftp deploy profile
File -> Settings -> Build, Execution, Deployment -> Add
Name: vagrant-deploy
Protocol: SFTP
IP: 192.168.33.101
Port: 22
Login: vagrant
Password: vagrant

click: Test SFTP Connection


3) Add Python interpreter:
Add remote, SSH
IP: 192.168.33.101
Port: 22
Login: vagrant
Password: vagrant
Python interpreter /home/vagrant/ansiblePower/venv/bin/python

