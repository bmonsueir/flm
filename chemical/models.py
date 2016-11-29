#chemical
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Chemical(models.Model):
    name = models.CharField( max_length=255,)
    description = models.CharField( max_length=255, )
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255, )
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('chemical: chemical', {'pk': self.pk })
    
    def __str__(self):
        return self.name 
        
    
class Specification(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,)
    max_value = models.CharField( max_length=255,)
    min_value = models.CharField(max_length=255,)
    test_method = models.CharField( max_length=255,)
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 

class Attribute(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,)
    description = models.CharField( max_length=255,)
    createdBy = models.ForeignKey(User, default=1)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 
        

        
