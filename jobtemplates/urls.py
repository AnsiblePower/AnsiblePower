from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.JobTemplatesIndex.as_view(), name='index'),
    url(r'^createjobtemplate', views.createJobTemplateForm.as_view(), name='createJobTemplate'),
]
