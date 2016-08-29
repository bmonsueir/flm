#chemical
from django.contrib import admin

# Register your models here.
from .models import Chemical, Specification, Attribute




admin.site.register(Chemical)
admin.site.register(Specification)

admin.site.register(Attribute)