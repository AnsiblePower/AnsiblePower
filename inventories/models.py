from django.db import models
from encrypted_fields import EncryptedCharField, EncryptedTextField


class Inventories(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    variables = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Groups(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    variables = models.TextField(null=True, blank=True)
    inventory = models.ManyToManyField(Inventories)

    def __unicode__(self):
        return self.name


class Hosts(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    ipAddress = models.GenericIPAddressField(null=True)
    port = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=255, null=True)
    variables = models.TextField(null=True, blank=True)
    hostKey = models.TextField(null=True)
    inventory = models.ManyToManyField(Inventories)
    group = models.ManyToManyField(Groups)
    credentials = models.ForeignKey('Credentials', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Credentials(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    keyOrPassword = models.NullBooleanField()
    privateKey = EncryptedTextField(null=True)
    publicKey = models.TextField(null=True)
    username = models.CharField(max_length=255, null=True)
    password = EncryptedCharField(max_length=255, null=True)

    def __unicode__(self):
        return self.name
