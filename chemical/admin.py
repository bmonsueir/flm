from django.contrib import admin

# Register your models here.
from .models import Chemical, Specification
from .models import Project
from .models import Formula, Batch

admin.site.register(Project)
admin.site.register(Chemical)
admin.site.register(Specification)
admin.site.register(Formula)
admin.site.register(Batch)