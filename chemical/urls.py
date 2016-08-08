from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.chemical_index, name = 'chemical_index'),
    url(r'^(?P<chemical_id>[0-9]+)/$', views.chemical_detail, name ='chemical_detail'),
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name ='project_detail'),
    url(r'^(?P<formula_id>[0-9]+)/$', views.formula_detail, name ='formula_detail'),
]