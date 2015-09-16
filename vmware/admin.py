from django.contrib import admin

# Register your models here.
from .models import Vcenter


class VcenterAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'date_created', 'date_modified')

admin.site.register(Vcenter, VcenterAdmin)