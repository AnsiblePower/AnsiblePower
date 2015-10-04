from django import forms
from .models import JobTemplates, validateFolder, validateYAML, playbookchoices
from projects.models import Projects


class CreateJobTemplateForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    project = forms.ModelChoiceField(queryset=Projects.objects.all(), validators=[validateFolder])
    extra_variables = forms.CharField(widget=forms.Textarea, validators=[validateYAML])
    playbook = forms.ChoiceField(choices=playbookchoices())

    class Meta:
        model = JobTemplates
        exclude = ['date_created', 'date_modified', ]





