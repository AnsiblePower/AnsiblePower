from django import forms
from .models import JobTemplates, validateFolder
from projects.models import Projects
from widgets import codemirror_widget




class CreateJobTemplateForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    project = forms.ModelChoiceField(queryset=Projects.objects.all(), validators=[validateFolder])
    extra_variables = forms.Textarea()

    class Meta:
        model = JobTemplates
        exclude = ['date_created', 'date_modified', ]

