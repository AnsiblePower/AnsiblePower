from django import forms
from django.core.exceptions import ValidationError
from .models import Hosts, Groups


class hostsField(forms.ModelMultipleChoiceField):
    pass

    def clean(self, value):
        key = self.to_field_name or 'pk'
        for pk in value:
            try:
                Hosts.objects.filter(**{key: pk})
            except (ValueError, TypeError):
                raise ValidationError(
                    self.error_messages['invalid_pk_value'],
                    code='invalid_pk_value',
                    params={'pk': pk},
                )
        qs = Hosts.objects.filter(**{'%s__in' % key: value})
        self.run_validators(value)
        return qs


class groupField(forms.ModelMultipleChoiceField):
    pass

    def clean(self, value):
        key = self.to_field_name or 'pk'
        for pk in value:
            try:
                Groups.objects.filter(**{key: pk})
            except (ValueError, TypeError):
                raise ValidationError(
                    self.error_messages['invalid_pk_value'],
                    code='invalid_pk_value',
                    params={'pk': pk},
                )
        qs = Groups.objects.filter(**{'%s__in' % key: value})
        self.run_validators(value)
        return qs
