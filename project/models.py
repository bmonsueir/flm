#project

from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime


class Project(models.Model):
    name = models.CharField( max_length=255,)
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('project: project', {'pk': self.pk })
    
    def __str__(self):
        return self.id 
        

class Group(models.Model):
    name = models.CharField( max_length=255,)
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255, )
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('project: group', {'pk': self.pk })
    
    def __str__(self):
        return self.name 
    