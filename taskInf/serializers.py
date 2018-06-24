# -*- coding: utf-8 -*-
from rest_framework import serializers
from taskInf.models import GenericTask, TaskOption

class GenericTaskSerializer(serializers.ModelSerializer):
  taskFrequency = serializers.CharField(source='get_taskFrequency_display', read_only=True)
  taskType = serializers.CharField(source='get_taskType_display', read_only=True)

  class Meta:
    model = GenericTask
    fields = ('id', 'taskOwner', 'taskName', 'taskFrequency', 'taskType', 'taskCreateTime', 'taskLastModifyTime')

class TaskOptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TaskOption
    fields = ('id', 'optionOwner', 'optionIDRelative', 'optionName', 'optionValue')
