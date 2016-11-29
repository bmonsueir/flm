#intro
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^register', views.register, name = 'register'),
    url(r'^tutorials', views.tutorials, name = 'tutorials'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    
]