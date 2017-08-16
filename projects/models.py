from django.db import models
from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

class Project(models.Model):
    name = models.CharField(max_length=225)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.ForeignKey('Company')
    is_archived = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.owner)


class Member(models.Model):
    project = models.ForeignKey('Project')
    worker = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.project.name, self.worker)

    class Meta:
        unique_together = ('project', 'worker')


class Log(models.Model):
    member = models.ForeignKey('Member')
    worker = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.member.project.name, self.worker)
