from django.views import generic
from .models import JobTemplates
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

