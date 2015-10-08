from django import forms
from django.core.validators import validate_ipv46_address
from .models import Inventories, Hosts, Groups ,validateYAML


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
    name = forms.CharField(max_length=255)
    ipAddress = forms.GenericIPAddressField(required=False)
    port = forms.IntegerField(max_value=65535, min_value=1, required=False)
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    group = forms.ModelChoiceField(queryset=Groups.objects.all(), widget=forms.HiddenInput, required=False)
    inventory = forms.ModelChoiceField(queryset=Inventories.objects.all(), widget=forms.HiddenInput)


    class Meta:
        model = Hosts
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, inv_pk, *args, **kwargs):
        super(CreateHostForm, self).__init__(*args, **kwargs)
        self.fields['inventory'].initial = inv_pk


class CreateGroupForm(CreateInventoryForm):
    #name = forms.CharField(max_length=255)
    inventory = forms.ModelChoiceField(queryset=Inventories.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Groups
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, inv_pk, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        self.fields['inventory'].initial = inv_pk