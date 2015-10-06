from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from .models import Inventories, Hosts
from .forms import CreateInventoryForm, CreateHostForm


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


class createHost(generic.CreateView):
    form_class = CreateHostForm
    model = Hosts
    template_name = 'inventories/createHost.html'
    # TODO: need to work with success url

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


class deleteInventory(generic.DeleteView):
    model = Inventories
    template_name = 'inventories/deleteInventory.html'
    success_url = '/inventories'

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})

