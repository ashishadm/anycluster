#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from anycluster import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^grid/(\d+)/(\d+)/$', views.getGrid, name='getGrid'),
    url(r'^kmeans/(\d+)/(\d+)/$', views.getPins, name='getPins'),
    url(r'^getbounds/$', views.getBounds, name='getBounds'),
    url(r'^getbounds/(\d+)/$', views.getBounds, name='getBounds_wsrid'),
    url(r'^getClusterContent/(\d+)/(\d+)/$', views.getClusterContent, name='getClusterContent'),
    url(r'^getAreaMarkers/(\d+)/(\d+)/$', views.getAreaMarkers, name='getAreaMarkers'),
    url(r'^getViewportMarkers/(\d+)/(\d+)/$', views.getViewportMarkers, name='getViewportMarkers'),
)
