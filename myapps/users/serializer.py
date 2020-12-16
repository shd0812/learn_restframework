#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/12/6 22:27
# @Author  cunfu
# @File serializer.py

from django.contrib.auth import models
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        max_length=20,
        min_length=6,
        help_text="确认密码",
        label="确认密码",
        write_only=True,
        error_messages={
            'min_length': "仅允许6到20个字符",
            'max_length': "仅允许6到20个字符"
        }
    )
    # token = serializers.CharField(label="token", read_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20位字符',
                    'max_length': '仅允许6-20位字符'
                }
            },
            'email': {
                'label': '邮箱',
                'write_only': True,
                'required': True,
                'validators': [UniqueValidator(queryset=models.User.objects.all(), message="邮箱不能重复")]
            },
            'password': {
                'label': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20位字符',
                    'max_length': '仅允许6-20位字符',
                }

            }
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise exceptions.ValidationError('两次输入密码不一致')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        res = models.User.objects.create_user(**validated_data)

        hanlder = api_settings.JWT_PAYLOAD_HANDLER
        encode_hanlder = api_settings.JWT_ENCODE_HANDLER

        playload = hanlder(res)
        token = encode_hanlder(playload)
        res.token = token
        return res


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['userid'] = self.user.id

        return data
