#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/18 08:21
# @Author  cunfu
# @File utils.py
from django.db.models import Count
# from apps.projects.models import Projects
# from apps.interfaces.models import Interfaces
# from apps.testcases.models import TestCases


def get_counts(data):

    # for item in data:
    #
    #     project_id = item['id']
    #     interface_count = Interfaces.objects.filter(project_id=project_id).count()
    #
    #     # interface_obj = Interfaces.objects.values('id').annotate(Count('testcase')).filter(project_id=project_id)
    #     # case_count = 0
    #     # for interface_sub in interface_obj:
    #     #     pass
    #     #
    #
    #
    #     interface = Interfaces.objects.filter(project_id=project_id).all()
    #     testcase_count = 0
    #     for sub_interface in interface:
    #         testcase_count += TestCases.objects.filter(interface_id=sub_interface.id).count()
    #     item['interface_count'] = interface_count
    #     item['testcase_count'] = testcase_count


    return data