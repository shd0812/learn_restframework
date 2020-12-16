#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/18 07:38
# @Author  cunfu
# @File pagenations.py
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    # Client can control the page using this query parameter.
    page_query_param = 'page'
    page_query_description = "第几页"

    # Client can control the page size using this query parameter.
    # Default is 'None'. Set to eg 'page_size' to enable usage.
    page_size_query_param = 'size'
    page_size_query_description = "多少条"

    # Set to an integer to limit the maximum page size the client may request.
    # Only relevant if 'page_size_query_param' has also been set.
    max_page_size = 6

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        print(response.data)
        current = self.page.number
        response.data['current'] = current
        total = self.page.paginator.num_pages
        response.data['total'] = total
        return response

