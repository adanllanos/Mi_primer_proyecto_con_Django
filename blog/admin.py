from django.contrib import admin
from .models import Project, Task, Laptop, Celular

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Laptop)
admin.site.register(Celular)

