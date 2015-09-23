from django.shortcuts import render

# Create your views here.
from .models import Vcenter, Vm
from django.views import generic
from pysphere import VIServer
from django.http import HttpResponse, HttpResponseRedirect
import vmvc
from .forms import ClonetForm, CreateVmForm
from django.views.generic.edit import FormView


class VcenterListView(generic.ListView):
    template_name = 'vmware/vcenterList.html'
    model = Vcenter


class VmListView(generic.ListView):
    model = Vm
    template_name = 'vmware/vmList.html'


# class VmCreateView(generic.CreateView):
#     model = Vm
#     template_name = 'vmware/vmCreate.html'
#     fields = ['vm_name']


def createVmView(request):
    if request.method == 'POST':
        form = CreateVmForm(request.POST)
        if form.is_valid():
            #TODO: Write Creating VM in model
            return HttpResponseRedirect('/vmware')
    else:
        form = CreateVmForm()
    return render(request, 'vmware/createVmForm.html', {'form': form})


def cloneView(request):
    if request.method == 'POST':
        form = ClonetForm(request.POST)
        if form.is_valid():
            print "vcenter cleaned data " + form.cleaned_data['vm_vcenter']
            return HttpResponseRedirect('/vmware')
    else:
        form = ClonetForm()
    return render(request, 'vmware/clone.html', {'form': form})


def vcenterTemplateList(request):
    vcenter = Vcenter.objects.get(pk=request.GET['vc_id'])
    template_names = vmvc.get_templates(vcenter)
    return render(request, 'vmware/vmList.html', {"vms": template_names})


def vcenterVmList(request):
    vcenter = Vcenter.objects.get(pk=request.GET['vc_id'])
    vm_list = vmvc.get_vms(vcenter)
    return render(request, 'vmware/vmList.html', {"vms": vm_list})


def pushFile(request):
    vcenter = Vcenter.objects.get(pk=1)
    vc = vmvc.connect_vcenter(vcenter)
    vm = vc.get_vm_by_name("dborysenko-test-vm")
    vm.login_in_guest("oracle", "qwer1234")
    files = vm.list_files("/users/oracle")
    vc.disconnect()
    return render(request, 'vmware/fileList.html', {"files": files})


def cloneVm(request):
    vcenter = Vcenter.objects.get(pk=1)
    vc = vmvc.connect_vcenter(vcenter)
    template = vc.get_vm_by_name(request.POST['template'])
    cluster_name = request.POST['vm_cluster_name']
    try:
        cluster = [k for k, v in vc.get_clusters().items() if v == cluster_name][0]
        resource_pool = vc.get_resource_pools(from_mor=cluster).items()[0][0]
    except IndexError, e:
        vc.disconnect()
        print "Error: Cannot find cluster - " + cluster_name
        print str(e)
    template.clone(request.POST['vm_name'], sync_run=False, power_on=False, resourcepool=resource_pool)
    vc.disconnect()
    return HttpResponse("<p>Done!<p>")


def getTemplateJs(request):
    if request.method == 'GET':
        templates = []
        vcenter = Vcenter.objects.get(pk=request.GET['vcenter_id'])
        template_list = vmvc.get_templates(vcenter)
        for template in template_list:
            templates.append('<option>' + template + '</option>')
        return HttpResponse(templates)
