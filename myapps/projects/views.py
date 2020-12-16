from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import action

from myapps.projects.models import Projects
from utils.utils import get_counts
from myapps.projects.serializer import ProjectsSerializer, ProjectSerializerNameandId

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ProjectsView(ModelViewSet):
    # permission_classes = (IsAuthenticated,)  # 인증 된 사용자만

    queryset = Projects.objects.all()

    serializer_class = ProjectsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = get_counts(serializer.data)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = get_counts(serializer.data)
        return Response(data)

    @action(detail=False)
    def names(self, request):
        query_set = self.get_queryset()
        data = self.get_serializer(query_set, many=True)
        return Response(data.data)

    def get_serializer_class(self):

        if self.action == 'names':
            return ProjectSerializerNameandId
        else:
            return ProjectsSerializer
