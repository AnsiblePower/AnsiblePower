# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobtemplates', '0002_auto_20151001_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtemplates',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Projects', null=True),
        ),
    ]
