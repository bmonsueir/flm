#chemical
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^chemical/(?P<chemical_id>[0-9]+)$', views.chemical, name='chemical'),
    url(r'chemicals/$', views.chemicals, name='chemicals'),
]