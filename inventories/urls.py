from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.InventoriesIndex.as_view(), name='index'),
    url(r'^createinventory', views.createInventory.as_view(), name='createInventory'),
    url(r'^editinventory/(?P<pk>\d+)', views.editInventory.as_view(), name='editInventory'),
    url(r'^deleteinventory/(?P<pk>\d+)', views.deleteInventory.as_view(), name='deleteInventory'),
    url(r'^manageinventory/(?P<pk>\d+)', views.manageInventory.as_view(), name='manageInventory'),
    url(r'^createhost/(?P<pk>\d+)', views.createHost.as_view(), name='createHost'),
    url(r'^edithost/(?P<pk>\d+)', views.editHost.as_view(), name='editHost'),
    url(r'^creategroup/(?P<pk>\d+)', views.createGroup.as_view(), name='createGroup'),
    url(r'^editgroup/(?P<pk>\d+)', views.editGroup.as_view(), name='editGroup'),
]
