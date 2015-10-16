# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobtemplates', '0004_auto_20151001_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtemplates',
            name='extra_variables',
            field=models.TextField(null=True, blank=True),
        ),
    ]
