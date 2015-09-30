from django import forms
from .models import Projects, validateFolder


class CreateProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    directory = forms.CharField(max_length=255, validators=[validateFolder])

    class Meta:
        model = Projects
        exclude = ['date_created', 'date_modified', ]



