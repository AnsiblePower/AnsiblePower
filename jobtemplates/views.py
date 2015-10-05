import os
import yaml
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from .models import JobTemplates, Projects
from .forms import CreateJobTemplateForm


class JobTemplatesIndex(generic.ListView):
    model = JobTemplates
    template_name = 'jobtemplates/jobTemplatesIndex.html'
    paginate_by = 5


class createJobTemplate(generic.CreateView):
    form_class = CreateJobTemplateForm
    template_name = 'jobtemplates/createJobTemplate.html'
    success_url = '/jobtemplates'


class editJobTemplate(generic.UpdateView):
    form_class = CreateJobTemplateForm
    model = JobTemplates
    template_name = 'jobtemplates/editJobTemplate.html'
    success_url = '/jobtemplates'


class deleteJobTemplate(generic.DeleteView):
    model = JobTemplates
    template_name = 'jobtemplates/deleteJobTemplate.html'
    success_url = '/jobtemplates'

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})


def runTest(request, **kwargs):
    if request.method == 'GET':
        template = JobTemplates.objects.get(pk=kwargs['pk'])
        yamlText = template.extra_variables
        yamlObj = yaml.load(yamlText)
        print yamlObj
        return HttpResponseRedirect('/jobtemplates')


def getJSONDirectory(request, **kwargs):
    if request.method == 'GET':
        proj = Projects.objects.get(pk=kwargs['pk'])
        result = {}
        i = 0
        try:
            for filename in os.listdir(proj.directory):
                if filename[-3:] == 'yml':
                    i += 1
                    result[i] = filename
        except OSError, e:
            print str(e)
        return JsonResponse(result)
