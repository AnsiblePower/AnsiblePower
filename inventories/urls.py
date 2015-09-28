from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.InventoriesIndex.as_view(), name='index'),
]