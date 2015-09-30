from django import forms
from .models import JobTemplates


class CreateJobTemplateForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)

    class Meta:
        model = JobTemplates
        exclude = ['date_created', 'date_modified', ]




