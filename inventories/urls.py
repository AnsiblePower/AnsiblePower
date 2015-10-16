from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.InventoriesIndex.as_view(), name='index'),
    url(r'^createinventory', views.createInventory.as_view(), name='createInventory'),
    url(r'^editinventory/(?P<pk>\d+)', views.editInventory.as_view(), name='editInventory'),
    url(r'^deleteinventory/(?P<pk>\d+)', views.deleteInventory.as_view(), name='deleteInventory'),
    url(r'^manageinventory/(?P<pk>\d+)', views.manageInventory.as_view(), name='manageInventory'),
    url(r'^createhost/$', views.createHost.as_view(), name='createHost'),
    url(r'^createhost/(?P<inv_id>\d+)/$', views.createHost.as_view(), name='createHost'),
    url(r'^edithost/(?P<pk>\d+)/$', views.editHost.as_view(), name='editHost'),
    url(r'^edithost/(?P<pk>\d+)/(?P<inv_id>\d+)/$', views.editHost.as_view(), name='editHost'),
    url(r'^groupindex/', views.groupIndex.as_view(), name='groupIndex'),
    url(r'^creategroup/$', views.createGroup.as_view(), name='createGroup'),
    url(r'^creategroup/(?P<inv_id>\d+)/$', views.createGroup.as_view(), name='createGroup'),
    url(r'^editgroup/(?P<pk>\d+)/$', views.editGroup.as_view(), name='editGroup'),
    url(r'^editgroup/(?P<pk>\d+)/(?P<inv_id>\d+)/$', views.editGroup.as_view(), name='editGroup'),
    url(r'^managegroup/(?P<pk>\d+)/$', views.manageGroup.as_view(), name='manageGroup'),
    url(r'^managegroup/(?P<pk>\d+)/(?P<inv_id>\d+)/$', views.manageGroup.as_view(), name='manageGroup'),
    url(r'^deletegroup/(?P<pk>\d+)/$', views.deleteGroup.as_view(), name='deleteGroup'),
    url(r'^deletegroup/(?P<pk>\d+)/(?P<inv_id>\d+)/$', views.deleteGroup.as_view(), name='deleteGroup'),
]
