from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)
