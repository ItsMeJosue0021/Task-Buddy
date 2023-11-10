from django.contrib import admin
from .models import UserProfile, Project, Task, ProjectMember

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
