# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
  userName = models.CharField('userName', max_length=128)
  userNickName = models.CharField('userNickName', max_length=128)

  class Meta:
    db_table = 'nn_user'

class GenericTask(models.Model):
  taskFrequencyChoices = (
    (0, '一次性'),
    (1, '周期性'),
  )

  taskTypeChoices = (
    (0, '投票'),
    (1, '反馈信息'),
    (2, '提醒'),
  )

  taskOwner = models.ForeignKey(User)
  taskName = models.CharField('taskName', max_length=128)
  taskFrequency = models.IntegerField('taskFrequency', default=0, choices=taskFrequencyChoices)
  taskType = models.IntegerField('taskType', default=2, choices=taskTypeChoices)
  taskCreateTime = models.DateTimeField('taskCreateTime', auto_now_add=True)
  taskLastModifyTime = models.DateTimeField('taskLastModifyTime', auto_now=True)

  class Meta:
    db_table = 'nn_task'

class TaskOption(models.Model):
  optionOwner = models.ForeignKey(GenericTask)
  optionIDRelative = models.IntegerField('optionIDRelative')
  optionName = models.CharField('optionName', max_length=128)
  optionValue = models.CharField('optionValue', max_length=512)

  class Meta:
    db_table = 'nn_option'

