# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vcenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('host_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=15)),
                ('user_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('vm_name', models.CharField(max_length=255)),
                ('vm_ip', models.GenericIPAddressField(null=True)),
                ('vm_subnet', models.GenericIPAddressField(null=True)),
                ('vm_gateway', models.GenericIPAddressField(null=True)),
                ('vm_hostname', models.CharField(max_length=255, null=True)),
                ('vcenter', models.ForeignKey(to='vmware.Vcenter')),
            ],
        ),
    ]
