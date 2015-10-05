from django.db import models
from django.core.exceptions import ValidationError
from projects.models import Projects
import yaml
from yaml.error import MarkedYAMLError
import os


class JobTemplates(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    run_type_choices = (
        ('run', 'Run'),
        ('check', 'Check'),
        ('scan', 'Scan'),
    )
    run_types = models.CharField(max_length=5,
                                 choices=run_type_choices,
                                 default='run')
    project = models.ForeignKey(Projects, null=True, on_delete=models.SET_NULL)
    playbook = models.CharField(max_length=255, null=True)
    extra_variables = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


def validateFolder(value):
    proj = Projects.objects.get(pk=value.pk)
    if os.path.isdir(proj.directory) and os.access(proj.directory, os.W_OK):
        return True
    else:
        raise ValidationError('%s project\'s directory %s not accessible' % (value, proj.directory))


def validateYAML(yamlText):
    try:
        yaml.load(yamlText)
        return True
    except MarkedYAMLError, e:
        raise ValidationError('YAML syntax error: %s' % str(e))


# def playbookchoices():
#     projects = Projects.objects.all()
#     result = []
#     i = 0
#     for proj in projects:
#         try:
#             directory = proj.directory
#             files = os.listdir(directory)
#             for filename in files:
#                 if filename[-3:] == 'yml':
#                     result.append((filename, filename))
#         except OSError, e:
#             pass
#     return result


def playbookchoices(directory):
    result = [('', '-----'), ]
    try:
        files = os.listdir(directory)
        for filename in files:
            if filename[-3:] == 'yml':
                result.append((filename, filename))
    except OSError, e:
        pass
    return result
