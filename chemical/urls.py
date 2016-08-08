from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<chemical_id>[0-9]+)/$', views.chemical_detail, name ='chemical_detail'),
    url(r'^chemical/(?P<filter_by>[a-zA_Z]+)/$', views.chemical_index, name='chemical_index'),
]