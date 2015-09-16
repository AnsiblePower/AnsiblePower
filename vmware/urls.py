__author__ = 'dborysenko'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^showvms/$', views.show_vms, name='showvms'),
]