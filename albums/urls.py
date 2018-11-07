from django.conf.urls import url
from . import views
from django.utils import timezone
from django.urls import path

urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    
    url(r'^cancion/new/$', views.cancion_new, name='cancion_new'),
    url(r'^cancion/(?P<pk>[0-9]+)/$', views.cancion_detail,  name='cancion_detail'),
    url(r'^cancion/lista/$', views.cancion_list, name='cancion_list'),
    url(r'^cancion/(?P<pk>[0-9]+)/edit/$', views.cancion_edit, name='cancion_edit'),
    url(r'^cancion/(?P<pk>\d+)/remove/$', views.cancion_remove, name='cancion_remove'),

    url(r'^artista/new/$', views.artista_new, name='artista_new'),
    url(r'^artista/(?P<pk>[0-9]+)/$', views.artista_detail,  name='artista_detail'),
    url(r'^artista/lista/$', views.artista_list, name='artista_list'),
    url(r'^artista/(?P<pk>[0-9]+)/edit/$', views.artista_edit, name='artista_edit'),
    url(r'^artista/(?P<pk>\d+)/remove/$', views.artista_remove, name='artista_remove'),

    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail,  name='album_detail'),
    url(r'^album/lista/$', views.album_list, name='album_list'),
    url(r'^album/(?P<pk>[0-9]+)/edit/$', views.album_edit, name='album_edit'),
    url(r'^album/(?P<pk>\d+)/remove/$', views.album_remove, name='album_remove'),
    ]   