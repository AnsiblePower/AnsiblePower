# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobtemplates', '0003_auto_20151001_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtemplates',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='projects.Projects', null=True),
        ),
    ]
