from django.db import models
from django.core.urlresolvers import reverse


class Projects(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    directory = models.CharField(max_length=255)
