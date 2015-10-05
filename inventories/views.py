from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from .models import Inventories
from .forms import CreateInventoryForm


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


class deleteInventory(generic.DeleteView):
    model = Inventories
    template_name = 'inventories/deleteInventory.html'
    success_url = '/inventories'

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})
