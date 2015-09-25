__author__ = 'dborysenko'
from ansible.playbook import PlayBook
from ansible.inventory import Inventory, Group, Host
from ansible import callbacks, inventory
from ansible import utils

import ansible.constants as C
import jinja2
from tempfile import NamedTemporaryFile
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C.DEFAULT_ROLES_PATH = os.path.join(BASE_DIR, 'roles')

def testRolleRun():
    utils.VERBOSITY = 3
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    stats = callbacks.AggregateStats()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    # hosts = ['dborrac1.ea.intropro.com']
    myInventory = Inventory()
    host = 'dborrac1.ea.intropro.com'
    group = 'appSERVERS'
    hosts = Host(host)
    groups = Group(group)
    myInventory.groups = [groups, ]
    groups.add_host(hosts)
    local = True
    gather_facts = True

    if gather_facts:
        gather_facts = 'yes'
    else:
        gather_facts = 'no'
    if local:
        hosts.set_variable('ansible_connection', 'local')


    role = 'bfmartin.ssh_known_hosts'
    hostsPlay = 'appSERVERS'

    extraVars = {
        'ssh_known_hosts': [
            {'name': host,
            'state': 'present',
            'aliases': [host.split('.')[0], ]},
        ],
        'ssh_known_hosts_path': '~vagrant/.ssh/known_hosts',
    }

    playbookContent = """---
    - hosts: %s
      gather_facts: %s
      roles:
         - %s
    """ % (hostsPlay, gather_facts, role)
    tempFile = NamedTemporaryFile(delete=False)
    tempFile.write(playbookContent)
    tempFile.close()

    pb = PlayBook(
        playbook=tempFile.name,
        inventory=myInventory,     # Our hosts, the rendered inventory file
        remote_user='root',
        remote_pass='qwer1234',
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        stats=stats,
        extra_vars=extraVars,
        #private_key_file='/path/to/key.pem'
    )

    pb.run()
    os.remove(tempFile.name)


def test():
    print BASE_DIR


if __name__ == "__main__":
    #getRepos()
    testRolleRun()
    #test()