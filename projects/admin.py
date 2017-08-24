from django.contrib import admin

from .models import Project, Member, Log

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Log)
