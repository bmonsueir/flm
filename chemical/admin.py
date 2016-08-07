from django.contrib import admin

# Register your models here.
from .models import Chemical, Specification


admin.site.register(Chemical)
admin.site.register(Specification)
