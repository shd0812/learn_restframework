#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/12/6 23:03
# @Author  cunfu
# @File serializer.py

from myapps.projects.models import Projects
from rest_framework import serializers
from myapps.debugtalks.models import DebugTalks


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('update_time', 'is_delete')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = Projects.objects.create(**validated_data)
        DebugTalks.objects.create(project=project)
        return project


class ProjectSerializerNameandId(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'name')
