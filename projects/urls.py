from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectIndex.as_view(), name='index'),
    url(r'^createproject', views.createProjectForm, name='createProject'),
    url(r'^dropproject', views.dropProject, name='dropProject'),
]