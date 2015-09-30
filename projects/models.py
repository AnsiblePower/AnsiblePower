from django.db import models
from django.core.exceptions import ValidationError
import os


class Projects(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    directory = models.CharField(max_length=255)


def validateFolder(value):
    if os.path.isdir(value) and os.access(value, os.W_OK):
        pass
    else:
        raise ValidationError('%s does not exist or not accessible' % value)