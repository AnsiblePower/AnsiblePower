from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Projects
from .forms import CreateProjectForm
# Create your views here.


class ProjectIndex(generic.ListView):
    model = Projects
    template_name = 'projects/projectsIndex.html'


def createProjectForm(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            proj = Projects(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
                            directory=form.cleaned_data['directory'])
            proj.save()
            return HttpResponseRedirect('/projects')
    else:
        form = CreateProjectForm()
    return render(request, 'projects/createProject.html', {'form': form})


def dropProject(request):
    #TODO: implement drop project object logic...
    pass



