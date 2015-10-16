# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '__first__'),
        ('jobtemplates', '0005_auto_20151002_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtemplates',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='inventories.Inventories', null=True),
        ),
    ]
