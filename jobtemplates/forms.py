from django import forms
from .models import JobTemplates, validateFolder
from projects.models import Projects
from codemirror import CodeMirrorTextarea

codemirror_widget = CodeMirrorTextarea(mode="python", theme="dracula", config={'fixedGutter': True})


class CreateJobTemplateForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    project = forms.ModelChoiceField(queryset=Projects.objects.all(), validators=[validateFolder])
    extra_variables = forms.CharField(required=False, widget=codemirror_widget)

    class Meta:
        model = JobTemplates
        exclude = ['date_created', 'date_modified', ]

