from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<chemical_id>[0-9]+)/$', views.chemical_detail, name ='chemical_detail'),
    url(r'^chemical/$', views.chemical_index, name='chemical_index'),
    url(r'^(?P<formula_id>[0-9]+)/$', views.formula_detail, name ='formula_detail'),
    url(r'^formula/$', views.formula_index, name='formula_index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name ='project_detail'),
    url(r'^project/$', views.project_index, name='project_index'),
    url(r'^tutorials/$', views.tutorials, name='tutorials'),
]