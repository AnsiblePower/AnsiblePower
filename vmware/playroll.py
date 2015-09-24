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
    utils.VERBOSITY = 0
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    stats = callbacks.AggregateStats()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    # hostsInv = ['dborrac1.ea.intropro.com']
    hostsInv = 'dborrac1.ea.intropro.com'
    myInventory = Inventory()
    groups = Group('appSERVERS')
    # groups.add_host(Host(hostsInv))
    myInventory.groups = [groups, ]
    groups.add_host(Host(hostsInv))

    role = 'adriagalin.motd'

    hostsPlay = 'appSERVERS'
    playbookContent = """---
    - hosts: %s
      gather_facts: no
      remote_user: oracle
      roles:
         - %s
    """ % (hostsPlay, role)
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
        #private_key_file='/path/to/key.pem'
    )

    pb.run()

def test():
    print BASE_DIR


if __name__ == "__main__":
    #getRepos()
    testRolleRun()
    #test()