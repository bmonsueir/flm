#chemical
from django.contrib import admin

from .models import Chemical, Specification, Attribute

admin.site.register(Chemical)
admin.site.register(Specification)
admin.site.register(Attribute)