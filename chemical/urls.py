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
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^batch/(?P<formula_id>[0-9]+)$', views.batch, name='batch'),
    url(r'^read_batch/(?P<formula_id>[0-9]+)$', views.read_batch, name='read_batch'),
    url(r'^add_batch/(?P<formula_id>[0-9]+)$', views.add_batch, name='add_batch'),
    url(r'^tutorials/$', views.tutorials, name='tutorials'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
   
]