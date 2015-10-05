from django.views import generic
from django.http import JsonResponse
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

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})
