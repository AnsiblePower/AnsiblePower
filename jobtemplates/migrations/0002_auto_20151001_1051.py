# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '__first__'),
        ('jobtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtemplates',
            name='extra_variables',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobtemplates',
            name='playbook',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jobtemplates',
            name='project',
            field=models.ForeignKey(to='projects.Projects', null=True),
        ),
        migrations.AddField(
            model_name='jobtemplates',
            name='run_types',
            field=models.CharField(default=b'run', max_length=5, choices=[(b'run', b'Run'), (b'check', b'Check'), (b'scan', b'Scan')]),
        ),
    ]
