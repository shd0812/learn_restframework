#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/12/6 23:04
# @Author  cunfu
# @File urls.py

from django.urls import path
from myapps.projects import views


urlpatterns = [
    path('name/', views.ProjectsView.as_view({'get': 'names'})),

    path('projects/', views.ProjectsView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/interfaces/', views.ProjectsView.as_view(
        {'get': 'retrieve', "delete": "destroy", 'put': "update", "patch": "partial_update", })),

]