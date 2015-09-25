#!/usr/bin/env bash

apt-get update
apt-get install -y python2.7
alias python=python2.7
apt-get install -y sshpass
apt-get install -y python-dev
apt-get install -y ansible
apt-get install -y python-setuptools
apt-get install -y python-virtualenv
easy_install pip

virtualenv django
chown -R vagrant:vagrant ~vagrant/django
cd django
source bin/activate
pip install Django GitPython Jinja2 MarkupSafe PyYAML ansible ansible-role-manager argparse colorama django-crispy-forms gitdb hgapi paramiko pycrypto pysphere requests semantic-version smmap wsgiref
#pip install Django==1.8.4, GitPython==0.3.2.RC1, Jinja2==2.8, MarkupSafe==0.23, PyYAML==3.11, ansible==1.9.3, ansible-role-manager==0.4, argparse==1.2.1, colorama==0.3.3, django-crispy-forms==1.5.2, gitdb==0.6.4, hgapi==1.7.2, paramiko==1.15.2, pycrypto==2.6.1, pysphere==0.1.7, requests==2.7.0, semantic-version==2.4.2, smmap==0.9.0, wsgiref==0.1.2

