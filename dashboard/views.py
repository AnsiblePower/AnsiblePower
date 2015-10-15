from django.shortcuts import render
from django.views import generic

# Create your views here.


class DashboardView(generic.TemplateView):
    template_name = 'dashboard/index.html'

