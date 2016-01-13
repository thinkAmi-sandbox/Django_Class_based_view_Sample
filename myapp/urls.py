from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ItemRedirect.as_view(), name='item-redirect'),
    url(r'^create/$', views.ItemCreate.as_view(), name='item-create'),
    url(r'^list/$', views.ItemList.as_view(), name='item-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ItemDetail.as_view(), name='item-detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ItemUpdate.as_view(), name='item-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name='item-delete'),
]
