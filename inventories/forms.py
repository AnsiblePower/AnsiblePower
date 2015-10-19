from django import forms
from .models import Inventories, Hosts, Groups
from .fieldValidators import validateYAML
from .widget import SelectHosts, SelectGroups
from .fields import hostsField, groupField


class CreateInventoryForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    variables = forms.CharField(widget=forms.Textarea, validators=[validateYAML], required=False)
    groups = groupField(queryset=Groups.objects.all(), required=False, widget=SelectGroups)
    hosts = hostsField(queryset=Hosts.objects.all(), required=False, widget=SelectHosts)

    class Meta:
        model = Inventories
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, *args, **kwargs):
        super(CreateInventoryForm, self).__init__(*args, **kwargs)
        self.fields['groups'].initial = Groups.objects.filter(inventory=self.instance.pk)
        self.fields['hosts'].initial = Hosts.objects.filter(inventory=self.instance.pk)
        # Check if form is using for update view and prefill fields:
        if self.initial:
            if self.instance.variables == '':
                self.initial['variables'] = '---'
        else:
            self.initial['variables'] = '---'

    def save(self, commit=True):
        # Check if this form for create group or for update (edit)
        if self.instance.pk:
            # Check if form was modified
            if self.has_changed():
                print "CHANGED"
                inventory = self.instance
                form_hosts_ids = []
                db_hosts_ids = []
                for host in self.cleaned_data['hosts']:
                    form_hosts_ids.append(host.pk)
                for host in self.fields['hosts'].initial:
                    db_hosts_ids.append(host.pk)
                # Check if host lists was modified
                if cmp(db_hosts_ids, form_hosts_ids) != 0:
                    delete = set(db_hosts_ids).difference(form_hosts_ids)
                    add = set(form_hosts_ids).difference(db_hosts_ids)
                    # Delete Host from Group
                    if delete:
                        hostdel = Hosts.objects.filter(pk__in=delete)
                        print "Delete: " + str(hostdel)
                        inventory.hosts_set.remove(*hostdel)
                    # Add Host to Group
                    if add:
                        hostadd = Hosts.objects.filter(pk__in=add)
                        print "Add: " + str(hostadd)
                        inventory.hosts_set.add(*hostadd)

                form_group_ids = []
                db_group_ids = []
                for group in self.cleaned_data['groups']:
                    form_group_ids.append(group.pk)
                for group in self.fields['groups'].initial:
                    db_group_ids.append(group.pk)
                if cmp(db_group_ids, form_group_ids) != 0:
                    delete = set(db_group_ids).difference(form_group_ids)
                    add = set(form_group_ids).difference(db_group_ids)
                    if delete:
                        groupdel = Groups.objects.filter(pk__in=delete)
                        print "Delete: " + str(groupdel)
                        inventory.groups_set.remove(*groupdel)
                    if add:
                        groupadd = Groups.objects.filter(pk__in=add)
                        print "Add: " + str(groupadd)
                        inventory.groups_set.add(*groupadd)

        super(CreateInventoryForm, self).save()


class CreateHostForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
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

    def __init__(self, inv_id=None, *args, **kwargs):
        super(CreateHostForm, self).__init__(*args, **kwargs)
        if inv_id:
            self.fields['inventory'].initial = inv_id
        if self.initial:
            if self.instance.variables == '':
                self.initial['variables'] = '---'
        else:
            self.initial['variables'] = '---'

    def save(self, commit=True):
        if self.fields['inventory'].initial:
            self.cleaned_data['inventory'] = self.fields['inventory'].initial
        super(CreateHostForm, self).save()


class CreateGroupForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    inventory = forms.ModelMultipleChoiceField(queryset=Inventories.objects.all(),
                                               #widget=forms.HiddenInput,
                                               required=False)
    description = forms.CharField(max_length=255, required=False)
    hosts = hostsField(queryset=Hosts.objects.all(), required=False, widget=SelectHosts)

    class Meta:
        model = Groups
        exclude = ['date_created', 'date_modified', ]

    def __init__(self, inv_id=None, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        self.fields['hosts'].initial = Hosts.objects.filter(group=self.instance.pk)
        if inv_id:
            self.fields['inventory'].initial = inv_id
        if self.initial:
            if self.instance.variables == '':
                self.initial['variables'] = '---'
        else:
            self.initial['variables'] = '---'

    def save(self, commit=True):
        print "SAVE"
        if self.fields['inventory'].initial:
            self.cleaned_data['inventory'] = self.fields['inventory'].initial
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



