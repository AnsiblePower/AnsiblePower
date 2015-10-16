from django.forms import SelectMultiple
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class SelectHosts(SelectMultiple):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = []
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select name="hosts" id="HostSearch" class="form-control" size="8" multiple="multiple">')]
        options = self.render_options(choices, value)
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe('\n'.join(output))


class SelectGroups(SelectMultiple):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = []
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select name="groups" id="GroupSearch" class="form-control" size="8" multiple="multiple">')]
        options = self.render_options(choices, value)
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe('\n'.join(output))