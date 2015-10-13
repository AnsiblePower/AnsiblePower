from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from .models import Inventories, Hosts, Groups
from .forms import CreateInventoryForm, CreateHostForm, CreateGroupForm
from Crypto.PublicKey import RSA
import paramiko
import socket


class InventoriesIndex(generic.ListView):
    model = Inventories
    template_name = 'inventories/inventoriesIndex.html'
    paginate_by = 5


class createInventory(generic.CreateView):
    form_class = CreateInventoryForm
    template_name = 'inventories/createInventory.html'
    success_url = '/inventories'


class editInventory(generic.UpdateView):
    form_class = CreateInventoryForm
    model = Inventories
    template_name = 'inventories/editInventory.html'
    success_url = '/inventories'


class manageInventory(generic.DetailView):
    model = Inventories
    template_name = 'inventories/manageInventory.html'

    def get_context_data(self, **kwargs):
        context = super(manageInventory, self).get_context_data(**kwargs)
        inv_pk = context['object'].pk
        context['hosts_list'] = Hosts.objects.filter(inventory=inv_pk)
        context['group_list'] = Groups.objects.filter(inventory=inv_pk)
        return context


class editHost(generic.UpdateView):
    model = Hosts
    form_class = CreateHostForm
    template_name = 'inventories/editHost.html'

    def get_success_url(self):
        return reverse('inventories:manageInventory', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super(editHost, self).get_form_kwargs()
        kwargs['inv_pk'] = self.kwargs['pk']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(editHost, self).get_context_data(**kwargs)
        # context['inv_pk'] = Hosts.objects.get(pk=self.kwargs['pk']).inventory.
        context['inv_pk'] = Inventories.objects.filter(hosts__pk=self.kwargs['pk'])
        return context


class manageGroup(generic.UpdateView):
    model = Groups
    template_name = 'inventories/manageGroup.html'
    form_class = CreateGroupForm

    def get_form_kwargs(self):
        kwargs = super(manageGroup, self).get_form_kwargs()
        kwargs['inv_pk'] = self.kwargs['pk']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(manageGroup, self).get_context_data(**kwargs)
        context['hosts_list'] = Hosts.objects.filter(group=context['object'].pk)
        context['all_hosts'] = Hosts.objects.exclude(group=context['object'].pk)
        return context

    def get_success_url(self):
        return reverse('inventories:manageGroup', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        for choice in form.fields['hosts'].choices:
            print choice
        return super(manageGroup, self).form_valid(form)


class createHost(generic.CreateView):
    form_class = CreateHostForm
    model = Hosts
    template_name = 'inventories/createHost.html'

    # Adding to context (templates)
    def get_context_data(self, **kwargs):
        context = super(createHost, self).get_context_data(**kwargs)
        context['inv_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('inventories:manageInventory', kwargs={'pk': self.kwargs['pk']})

    # Adding to form class instantiating
    def get_form_kwargs(self):
        kwargs = super(createHost, self).get_form_kwargs()
        kwargs['inv_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if form.cleaned_data['port']:
            port = form.cleaned_data['port']
        else:
            port = 22
        if form.cleaned_data['ipAddress']:
            address = form.cleaned_data['ipAddress']
        else:
            address = form.cleaned_data['name']
        try:
            # known_hosts
            mySocket.connect((address, port))
            myTransport = paramiko.Transport(mySocket)
            myTransport.start_client()
            sshKey = myTransport.get_remote_server_key()
            myTransport.close()
            mySocket.close()

            # SSH key pairs
            new_key = RSA.generate(2048)
            form.instance.publicKey = new_key.publickey().exportKey(format='OpenSSH')
            form.instance.privateKey = new_key.exportKey()
            form.instance.hostKey = sshKey.get_base64()

            # Push public key to server
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(address, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            cmd = 'echo %s >> $HOME/.ssh/authorized_keys' % new_key.publickey().exportKey(format='OpenSSH')
            ssh.exec_command(cmd)
            ssh.close()

        except socket.error, e:
            print str(e)

        return super(createHost, self).form_valid(form)


class createGroup(generic.CreateView):
    form_class = CreateGroupForm
    model = Groups
    template_name = 'inventories/createGroup.html'

    def get_context_data(self, **kwargs):
        context = super(createGroup, self).get_context_data(**kwargs)
        context['inv_pk'] = self.kwargs['pk']
        return context

    def get_form_kwargs(self):
        kwargs = super(createGroup, self).get_form_kwargs()
        kwargs['inv_pk'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        return reverse('inventories:manageInventory', kwargs={'pk': self.kwargs['pk']})


class deleteInventory(generic.DeleteView):
    model = Inventories
    template_name = 'inventories/deleteInventory.html'
    success_url = '/inventories'

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})


def balanceGroup(request, *args, **kwargs):
    if request.method == 'POST':
        group = Groups.objects.get(pk=kwargs['pk'])
        for i in request.POST.getlist('from[]'):
            host = Hosts.objects.get(pk=i)
            host.group.add(group)
        return HttpResponseRedirect(reverse('inventories:manageGroup', kwargs={'pk': kwargs['pk']}))

