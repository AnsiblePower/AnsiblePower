from django.db import models


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
    hostKey = models.TextField(null=True)
    privateKey = models.TextField(null=True)
    publicKey = models.TextField(null=True)
    description = models.CharField(max_length=255, null=True)
    variables = models.TextField(null=True, blank=True)
    inventory = models.ManyToManyField(Inventories)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    group = models.ManyToManyField(Groups)

    def __unicode__(self):
        return self.name

