__author__ = 'dborysenko'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.VcenterListView.as_view(), name='index'),
    url(r'^vmList/$', views.VmListView.as_view(), name='vmList'),
    url(r'^vcentervmlist/$', views.vcenterVmList, name='vcenterVmList'),
    url(r'^vcentertemplatelist/$', views.vcenterTemplateList, name='vcenterTemplateList'),
    url(r'^filelist/$', views.pushFile, name='pushfile'),
    url(r'^cloneform/$', views.cloneView, name='cloneForm'),
    url(r'^clonevm/$', views.cloneVm, name='cloneVM'),
    url(r'^createvm/$', views.createVmView, name='createVmView'),
    url(r'^cloneform/gettemplatesjs', views.getTemplateJs, name='getTemplateJs'),
]
