# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:47:59 2017

@author: Evania
"""

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^services/$', views.ServiceListView.as_view(), name='services'),
    url(r'^service/(?P<pk>\d+)$', views.ServiceDetailView.as_view(), name='service-detail'),
    url(r'^userprofiles/$', views.UserProfileListView.as_view(), name='userprofiles'),
    url(r'^userprofiles/(?P<pk>\d+)$', views.UserProfileDetailView.as_view(), name='userprofiles-detail'),
]
