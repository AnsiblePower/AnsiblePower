from django import forms
from .models import Projects


class CreateProjectForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    directory = forms.CharField(max_length=255)

