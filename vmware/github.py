__author__ = 'dborysenko'
import requests
import json
import manageroles
import os

import ansible.constants as C
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def getRepos():
    req = requests.get('https://api.github.com/users/borisensx/repos')
    repoList = []
    if (req.ok):
        repoItems = json.loads(req.text or req.content)
        for repoItem in repoItems:
            print repoItem['name']
            repoList.append(repoItem['name'])
    return repoList


def installRole():
    role_path = os.path.join(BASE_DIR, 'roles')
    role_name = 'bfmartin.ssh_known_hosts'
    #manageroles.execute('init', ['-p', '/tmp', role_name])
    manageroles.execute('install', ['-p', role_path, role_name, ])


def env_var():
    #os.environ['ANSIBLE'] = 'Hello World'
    print C.DEFAULT_ROLES_PATH


if __name__ == "__main__":
    #getRepos()
    installRole()
    #env_var()