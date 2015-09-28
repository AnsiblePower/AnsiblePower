from django.contrib import admin

# Register your models here.
from .models import Vcenter, Vm


class VcenterAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'date_created', 'date_modified')


class VmAdmin(admin.ModelAdmin):
    list_display = ('vm_name', 'date_created', 'date_modified')

admin.site.register(Vcenter, VcenterAdmin)
admin.site.register(Vm, VmAdmin)