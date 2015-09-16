# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmware', '0002_auto_20150916_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('vm_name', models.CharField(max_length=255)),
                ('vcenter', models.ForeignKey(to='vmware.Vcenter')),
            ],
        ),
    ]
