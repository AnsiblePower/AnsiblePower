from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='index'),
]