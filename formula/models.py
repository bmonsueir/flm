#formula
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
from project.models import Project

        
class Formula(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    book = models.CharField( max_length=255,)
    tab = models.CharField( max_length=255, )
    header = models.CharField(max_length=255,)
    functions = models.CharField(max_length=255, )
    data = models.TextField(max_length=255, )
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255, )
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('formula: formula', {'pk': self.pk })
    
    def __str__(self):
        return self.book 

