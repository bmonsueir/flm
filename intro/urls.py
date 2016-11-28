#intro
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^login', views.login, name = 'login'),
]