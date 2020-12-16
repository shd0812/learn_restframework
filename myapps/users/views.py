from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from myapps.users.serializer import  RegisterSerializer, MyTokenObtainPairSerializer
# Create your views here.

# 注册的view
class RegisterView(CreateAPIView):

    # permission_classes = []
    serializer_class = RegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):

    # authentication_classes = []
    # permission_classes = []
    serializer_class = MyTokenObtainPairSerializer

