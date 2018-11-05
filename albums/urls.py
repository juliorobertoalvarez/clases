from django.conf.urls import url
from . import views
from django.utils import timezone
from django.urls import path

urlpatterns = [
    #url(r'^$', views.album_list, name='album_list'),

    #url(r'^artista/nuevo/$', views.artista_nuevo, name='artista_nuevo'),
    #path('artista/<int:pk>/', views.artista_detail, name='artista_detail'),
    #url(r'^artista/list/$', views.artista_list, name='artista_list'),
    #url(r'^artista/(?P<pk>[0-9]+)/edit/$', views.artista_editar, name='artista_editar'),
    #url(r'^artista/(?P<pk>[0-9]+)/remove/$', views.artista_remove, name='artista_remove'),

    #url(r'^album/nuevo/$', views.album_nuevo, name='album_nuevo'),
    #path('album/<int:pk>/', views.album_detail, name='album_detail'),
    #url(r'^album/list/$', views.album_list, name='album_list'),
    #url(r'^album/(?P<pk>[0-9]+)/edit/$', views.album_editar, name='album_editar'),
    #url(r'^album/(?P<pk>[0-9]+)/remove/$', views.album_remove, name='album_remove'),

    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^$', views.album_list, name='album_list'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail,  name='album_detail'),
    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^album/(?P<pk>[0-9]+)/edit/$', views.album_edit, name='album_edit'),
    url(r'^album/(?P<pk>\d+)/remove/$', views.album_remove, name='album_remove'),
    ]   