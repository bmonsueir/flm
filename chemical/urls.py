from django.conf.urls import url
from . import views

#workbook
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<chemical_id>[0-9]+)/$', views.chemical, name ='chemical'),
    url(r'^chemical/(?P<chemical_id>[0-9]+)$', views.chemical, name='chemical'),
    url(r'^chemicals/$', views.chemicals, name='chemicals'),
    url(r'^formulas/(?P<project_id>[0-9]+)$', views.formulas, name='formulas'),
    url(r'^group/(?P<group_id>[0-9]+)$', views.group, name='group'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.projects, name='projects'),
    url(r'^tutorials/$', views.tutorials, name='tutorials'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name = 'index'),
   
]