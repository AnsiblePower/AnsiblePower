from django.shortcuts import render
from django.views import generic
from .models import JobTemplates


class JobTemplatesIndex(generic.ListView):
    model = JobTemplates
    template_name = 'jobtemplates/jobTemplatesIndex.html'
