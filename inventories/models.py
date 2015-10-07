from django.db import models
from django.core.exceptions import ValidationError
from yaml.error import MarkedYAMLError
import yaml
import re

class Inventories(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    variables = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

def validateYAML(yamlText):
    try:
        yaml.load(yamlText)
        return True
    except MarkedYAMLError, e:
        raise ValidationError('YAML syntax error: %s' % str(e))


class Hosts(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    ipAddress = models.GenericIPAddressField(null=True)
    port = models.PositiveIntegerField(null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    variables = models.TextField(null=True, blank=True)
    inventory = models.ForeignKey(Inventories)

    def __unicode__(self):
        return self.name
