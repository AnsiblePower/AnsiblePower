from django import forms
from .models import JobTemplates, validateFolder, validateYAML, playbookchoices
from projects.models import Projects


class CreateJobTemplateForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    project = forms.ModelChoiceField(queryset=Projects.objects.all(), validators=[validateFolder])
    extra_variables = forms.CharField(widget=forms.Textarea, validators=[validateYAML], required=False)
    playbook = forms.CharField(widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(CreateJobTemplateForm, self).__init__(*args, **kwargs)
        # Check if form is using for update view and prefill fields:
        if self.initial:
            proj = Projects.objects.get(pk=self.initial['project'])
            playbooks = playbookchoices(proj.directory)
            self.fields['playbook'].widget.choices = playbooks
            # If somehow playbook field is out of scope we provide blank choice:
            if not (self.instance.playbook, self.instance.playbook) in playbooks:
                self.initial['playbook'] = playbooks[0]
            else:
                self.initial['playbook'] = self.instance.playbook

            if self.instance.extra_variables == '':
                self.initial['extra_variables'] = '---'
        else:
            self.initial['extra_variables'] = '---'


    class Meta:
        model = JobTemplates
        exclude = ['date_created', 'date_modified', ]





