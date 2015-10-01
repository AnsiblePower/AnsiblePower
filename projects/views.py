from django.views import generic
from django.http import HttpResponseServerError
from django.db import IntegrityError
from .models import Projects
from .forms import CreateProjectForm

# Create your views here.


class ProjectIndex(generic.ListView):
    model = Projects
    template_name = 'projects/projectsIndex.html'
    paginate_by = 5


class createProject(generic.CreateView):
    form_class = CreateProjectForm
    template_name = 'projects/createProject.html'
    success_url = '/projects'


class editProject(generic.UpdateView):
    form_class = CreateProjectForm
    template_name = 'projects/editProject.html'
    model = Projects
    success_url = '/projects'


class deleteProject(generic.DeleteView):
    model = Projects
    success_url = '/projects'
    template_name = 'projects/deleteProject.html'

    # def delete(self, request, *args, **kwargs):
    #     print "trying in views"
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     try:
    #         self.object.delete()
    #     except IntegrityError, e:
    #         return HttpResponseServerError('Hello World')






