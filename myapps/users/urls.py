#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/12/6 22:36
# @Author  cunfu
# @File urls.py
from django.urls import path, re_path
from myapps.users import views
from  rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)



urlpatterns = [


    # path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]