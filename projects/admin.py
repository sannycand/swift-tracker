from django.contrib import admin

from .models import Company, Project, Member, Log

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Log)
