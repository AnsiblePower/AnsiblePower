from django.shortcuts import render

# Create your views here.
from .models import Vcenter, Vm
from django.views import generic
from pysphere import VIServer
from django.http import HttpResponseRedirect
import ssl

class IndexView(generic.ListView):
    template_name = 'vcenter/index.html'
    vcenter_list = Vcenter.objects.order_by('-date_created')

    def get_queryset(self):
        return Vcenter.objects.all()


def connect_vcenter(vcenter):

    default_context = ssl._create_default_https_context
    server = VIServer()
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        server.connect(vcenter.host_name, vcenter.user_name, vcenter.user_password)
        return server
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


def show_vms(request):
    vcenter = Vcenter.objects.get(pk=request.POST['vc_id'])
    vc = connect_vcenter(vcenter)
    print vc.get_registered_vms()
    vc.disconnect()
