from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectIndex.as_view(), name='index'),
    url(r'^createproject', views.createProject.as_view(), name='createProject'),
    url(r'^deleteproject/(?P<pk>\d+)/$', views.deleteProject.as_view(), name='deleteProject'),
    url(r'^editroject/(?P<pk>\d+)/$', views.editProject.as_view(), name='editProject'),
]
