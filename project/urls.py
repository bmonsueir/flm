#project
from django.conf.urls import url
from . import views

#workbook
from django.conf import settings

urlpatterns = [
    url(r'^group/(?P<group_id>[0-9]+)$', views.group, name='group'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.projects, name='projects'),
]