#formulas
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^formulas/(?P<project_id>[0-9]+)$', views.formulas, name='formulas'),
]