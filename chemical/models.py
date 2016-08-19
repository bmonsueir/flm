from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Chemical(models.Model):
    name = models.CharField( max_length=255,)
    description = models.CharField( max_length=255, )
    functions = models.CharField(max_length=255, )
    codes = models.CharField(max_length=255, )
    regulatory = models.CharField(max_length=255, )
    updatedBy = models.CharField(max_length=255, )
    permissions = models.CharField(max_length=255, )
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('chemical: chemical_detail', {'pk': self.pk })
    
    def __str__(self):
        return self.name 
        
    
class Specification(models.Model):
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,)
    max_value = models.CharField( max_length=255,)
    min_value = models.CharField(max_length=255,)
    test_method = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255, )
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 
        
class Project(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField( max_length=255,)
    updatedBy = models.CharField(max_length=255,)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 
        
class Formula(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,)
    total = models.DecimalField(default = 100.0000, max_digits=7, decimal_places=4)
    locked = models.BooleanField(default = False)
    updatedBy = models.CharField(max_length=255,)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.name 
        
class Batch(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    phase = models.CharField(max_length=5,)
    amount = models.DecimalField(default = 0.0000, max_digits=7, decimal_places=4)
    instruction = models.CharField(max_length=255,)
    row = models.IntegerField()
    updatedBy = models.CharField(max_length=255,)
    permissions = models.CharField(max_length=255,)
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.instruction
class Workbook(models.Model):
    book = models.CharField( max_length=255,)
    tab = models.CharField( max_length=255, )
    header = models.CharField(max_length=255,)
    functions = models.CharField(max_length=255, )
    data = models.TextField(max_length=255, )
    updatedBy = models.CharField(max_length=255, )
    permissions = models.CharField(max_length=255, )
    updatedAt = models.DateTimeField('date created', default=datetime.now)
    
    def __str__(self):
        return self.book 
        