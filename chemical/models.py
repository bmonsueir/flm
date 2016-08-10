from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Chemical(models.Model):
    name = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255, default = "Admin",)
    permissions = models.CharField(max_length=255, default = "All",)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('chemical: chemical_detail', {'pk': self.pk })
    
    def __str__(self):
        return self.name 
        
class Attribute(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,)
    value = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255, default = "Admin",)
    permissions = models.CharField(max_length=255, default = "All",)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 
    
        
class Specification(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,)
    max_value = models.CharField( max_length=255,)
    min_value = models.CharField(max_length=255,)
    test_method = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255, default = "Admin",)
    permissions = models.CharField(max_length=255, default = "All",)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 
        
class Project(models.Model):
    name = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255,)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.CharField( max_length=255,)
    
    def __str__(self):
        return self.name 
        
class Formula(models.Model):
    name = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255,)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.CharField( max_length=255,)
    
    def __str__(self):
        return self.name