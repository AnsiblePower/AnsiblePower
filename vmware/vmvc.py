__author__ = 'dborysenko'
from pysphere import VIServer
from models import Vcenter
import ssl


def connect_vcenter(vcenter):
    #default_context = ssl._create_default_https_context
    server = VIServer()
    try:
        #ssl._create_default_https_context = ssl._create_unverified_context
        server.connect(vcenter.host_name, vcenter.user_name, vcenter.user_password)
        return server
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


def get_templates(vcenter):
    vc = connect_vcenter(vcenter)
    template_list = vc.get_registered_vms(advanced_filters={'config.template': True})
    template_names = []
    for template in template_list:
        name = template.split()[1].split('/')[0]
        template_names.append(name)
    vc.disconnect()
    return template_names


def get_vms(vcenter):
    vc = connect_vcenter(vcenter)
    vm_list = vc.get_registered_vms(advanced_filters={'config.template': False})
    vm_names = []
    for vm in vm_list:
        name = vm.split()[1].split('/')[0]
        vm_names.append(name)
    vc.disconnect()
    return vm_names

def get_vcenters():
    result = []
    all_vcenters = Vcenter.objects.all()
    for vcenter in all_vcenters:
        result.append((vcenter._get_pk_val(), vcenter.host_name))
    return result
