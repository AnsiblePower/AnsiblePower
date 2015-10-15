from django import forms
from .models import Inventories, Hosts, Groups
from .fieldValidators import validateYAML
from .widget import SelectMultipleCust
from .fields import hostsField


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
    group = forms.ModelMultipleChoiceField(queryset=Groups.objects.all(),
                                           widget=forms.HiddenInput, required=False)
    inventory = forms.ModelMultipleChoiceField(queryset=Inventories.objects.all(),
                                               required=False)
    hostKey = forms.CharField(widget=forms.HiddenInput, required=False)
    publicKey = forms.CharField(widget=forms.HiddenInput, required=False)
    privateKey = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Hosts
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, inv_pk, *args, **kwargs):
        super(CreateHostForm, self).__init__(*args, **kwargs)
        self.fields['inventory'].initial = inv_pk

    def save(self, commit=True):
        super(CreateHostForm, self).save()


class CreateGroupForm(CreateInventoryForm):
    inventory = forms.ModelChoiceField(queryset=Inventories.objects.all(), widget=forms.HiddenInput, required=False)
    hosts = hostsField(queryset=Hosts.objects.all(), required=False, widget=SelectMultipleCust)

    class Meta:
        model = Groups
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        #self.fields['inventory'].initial = inv_pk
        self.fields['hosts'].initial = Hosts.objects.filter(group=self.instance.pk)
        # Check if form is using for update view and prefill fields:

    def save(self, commit=True):
        # Check if this form for create group or for update (edit)
        if self.instance.pk:
            # Check if form was modified
            if self.has_changed():
                print "CHANGED"
                group = self.instance
                form_ids = []
                db_ids = []
                for host in self.cleaned_data['hosts']:
                    form_ids.append(host.pk)
                for host in self.fields['hosts'].initial:
                    db_ids.append(host.pk)
                # Check if host lists was modified
                if cmp(db_ids, form_ids) != 0:
                    delete = set(db_ids).difference(form_ids)
                    add = set(form_ids).difference(db_ids)
                    # Delete Host from Group
                    if delete:
                        hostdel = Hosts.objects.filter(pk__in=delete)
                        print "Delete: " + str(hostdel)
                        group.hosts_set.remove(*hostdel)
                    # Add Host to Group
                    if add:
                        hostadd = Hosts.objects.filter(pk__in=add)
                        print "Add: " + str(hostadd)
                        group.hosts_set.add(*hostadd)

        super(CreateGroupForm, self).save()



