from django import forms
from django.core.validators import validate_ipv46_address
from .models import Inventories, Hosts, validateYAML


class CreateInventoryForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    variables = forms.CharField(widget=forms.Textarea, validators=[validateYAML], required=False)

    class Meta:
        model = Inventories
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, *args, **kwargs):
        super(CreateInventoryForm, self).__init__(*args, **kwargs)
        # Check if form is using for update view and prefill fields:
        if self.initial:
            if self.instance.variables == '':
                self.initial['variables'] = '---'
        else:
            self.initial['variables'] = '---'


class CreateHostForm(CreateInventoryForm):
    name = forms.CharField(max_length=255, validators=[validate_ipv46_address])
    inventory = forms.ModelChoiceField(queryset=Inventories.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Hosts
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, inv_pk, *args, **kwargs):
        super(CreateHostForm, self).__init__(*args, **kwargs)
        self.fields['inventory'].initial = inv_pk

