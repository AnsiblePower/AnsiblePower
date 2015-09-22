from django.db import models

# Create your models here.


class Vcenter(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    host_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=15)

    def __unicode__(self):
        return self.host_name


class Vm(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    vm_name = models.CharField(max_length=255)
    vm_ip = models.GenericIPAddressField(null=True)
    vm_subnet = models.GenericIPAddressField(null=True)
    vm_gateway = models.GenericIPAddressField(null=True)
    vm_hostname = models.CharField(max_length=255, null=True)
    vcenter = models.ForeignKey(Vcenter)

    def __unicode__(self):
        return self.vm_name
