# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from taskInf import views

router = routers.DefaultRouter()
router.register(r'tasks', views.GenericTaskViewSet)
router.register(r'options', views.TaskOptionViewSet)

# api url 配置
urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
