from django.views import generic
from .models import JobTemplates
from .forms import CreateJobTemplateForm

class JobTemplatesIndex(generic.ListView):
    model = JobTemplates
    template_name = 'jobtemplates/jobTemplatesIndex.html'
    paginate_by = 5


class createJobTemplateForm(generic.CreateView):
    form_class = CreateJobTemplateForm
    template_name = 'jobtemplates/createJobTemplate.html'
    success_url = '/jobtemplates'