from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from .models import Inventories, Hosts, Groups
from .forms import CreateInventoryForm, CreateHostForm, CreateGroupForm


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
        context['hosts_list'] = Hosts.objects.all()
        # TODO: implement hostgroup queryset (http://stackoverflow.com/a/12357483)
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
        context['inv_pk'] = self.kwargs['pk']
        return context


class createHost(generic.CreateView):
    form_class = CreateHostForm
    model = Hosts
    template_name = 'inventories/createHost.html'

    def get_context_data(self, **kwargs):
        context = super(createHost, self).get_context_data(**kwargs)
        context['inv_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('inventories:manageInventory', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super(createHost, self).get_form_kwargs()
        kwargs['inv_pk'] = self.kwargs['pk']
        return kwargs


class createGroup(createHost):
    form_class = CreateGroupForm
    model = Groups
    template_name = 'inventories/createGroup.html'


class deleteInventory(generic.DeleteView):
    model = Inventories
    template_name = 'inventories/deleteInventory.html'
    success_url = '/inventories'

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})

