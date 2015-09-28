from django.shortcuts import render
from django.views import generic


class InventoriesIndex(generic.TemplateView):
    template_name = 'inventories/inventoriesIndex.html'