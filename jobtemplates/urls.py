from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.JobTemplatesIndex.as_view(), name='index'),
]
