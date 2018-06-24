# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

from taskInf.models import GenericTask, TaskOption
from rest_framework import viewsets
from taskInf.serializers import GenericTaskSerializer, TaskOptionSerializer

class GenericTaskViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  def list(self, request):
    queryset = GenericTask.objects.all()
    serializer = GenericTaskSerializer(queryset, many=True)
    return Response(serializer.data)

  queryset = GenericTask.objects.all()
  serializer_class = GenericTaskSerializer

class TaskOptionViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = TaskOption.objects.all()
  serializer_class = TaskOptionSerializer
