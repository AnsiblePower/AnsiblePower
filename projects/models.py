from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
import os


class Projects(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    directory = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    # def delete(self, using=None):
    #     try:
    #         self.delete(using=None)
    #     except ProtectedError, e:
    #         raise Exception('Hello World from models')


def validateFolder(value):
    if os.path.isdir(value) and os.access(value, os.W_OK):
        pass
    else:
        raise ValidationError('%s does not exist or not accessible' % value)
