from django.conf.urls import url
from . import views

#workbook
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<chemical_id>[0-9]+)/$', views.chemical_detail, name ='chemical_detail'),
    url(r'^project/(?P<project_id>[0-9]+)/$', views.project_detail, name ='project_detail'),
    url(r'^chemical/$', views.chemical_index, name='chemical_index'),
    url(r'^(?P<formula_id>[0-9]+)/$', views.formula_detail, name ='formula_detail'),
    url(r'^formula/$', views.formula_index, name='formula_index'),
    url(r'^project/$', views.project_index, name='project_index'),
    url(r'^create_chemical/$', views.create_chemical, name='create_chemical'),
    url(r'^create_formula/(?P<project_id>[0-9]+)$', views.create_formula, name='create_formula'),
    url(r'^batch/(?P<formula_id>[0-9]+)$', views.batch, name='batch'),
    url(r'^create_project/$', views.create_project, name='create_project'),
    url(r'^create_attribute/(?P<chemical_id>[0-9]+)/$', views.create_attribute, name='create_attribute'),
    url(r'^create_specification/(?P<chemical_id>[0-9]+)/$', views.create_specification, name='create_specification'),
    url(r'^tutorials/$', views.tutorials, name='tutorials'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
   
]