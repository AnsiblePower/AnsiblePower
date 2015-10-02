from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.JobTemplatesIndex.as_view(), name='index'),
    url(r'^createjobtemplate', views.createJobTemplate.as_view(), name='createJobTemplate'),
    url(r'^editjobtemplate/(?P<pk>\d+)', views.editJobTemplate.as_view(), name='editJobTemplate'),
    url(r'^deletejobtemplate/(?P<pk>\d+)', views.deleteJobTemplate.as_view(), name='deleteJobTemplate'),
    url(r'^runjobtemplate/(?P<pk>\d+)', views.runTest, name='runJobTemplate'),
    url(r'^getjsondirectory/(?P<pk>\d+)', views.getJSONDirectory, name='getJSONDirectory'),
]
