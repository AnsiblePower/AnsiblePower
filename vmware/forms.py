__author__ = 'dborysenko'
from django import forms
import vmvc
from models import Vcenter


class ClonetForm(forms.Form):
    vm_name = forms.CharField(max_length=255)
    vm_ip = forms.GenericIPAddressField(required=False)
    vm_subnet = forms.GenericIPAddressField(required=False)
    vm_gateway = forms.GenericIPAddressField(required=False)
    vm_hostname = forms.CharField(max_length=255, required=False)
    vm_cluster_name = forms.CharField(max_length=255)


    templates = (
        ('dborysenko-test-template', 'dborysenko-test-template'),
    )
    template = forms.ChoiceField(choices=templates)
    vm_vcenter = forms.ChoiceField(vmvc.get_vcenters())


class CreateVmForm(forms.Form):
    vm_name = forms.CharField(max_length=255)
    vm_ip = forms.GenericIPAddressField(required=False)
    vm_subnet = forms.GenericIPAddressField(required=False)
    vm_gateway = forms.GenericIPAddressField(required=False)
    vm_hostname = forms.CharField(max_length=255, required=False)

