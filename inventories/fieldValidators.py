from django.core.exceptions import ValidationError
from yaml.error import MarkedYAMLError
import yaml


def validateYAML(yamlText):
    try:
        yaml.load(yamlText)
        return True
    except MarkedYAMLError, e:
        raise ValidationError('YAML syntax error: %s' % str(e))
