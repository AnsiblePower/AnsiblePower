#!/usr/bin/env bash

apt-get update
apt-get install -y python2.7
alias python=python2.7
apt-get install -y sshpass
apt-get install -y python-dev
apt-get install -y ansible
apt-get install -y python-setuptools
easy_install pip

virtualenv django
cd django
source bin/activate
pip install Django, GitPython, Jinja2, MarkupSafe, PyYAML, ansible, ansible-role-manager, argparse, colorama, django-crispy-forms, gitdb, hgapi, paramiko, pycrypto, pysphere, requests, semantic-version, smmap, wsgiref

