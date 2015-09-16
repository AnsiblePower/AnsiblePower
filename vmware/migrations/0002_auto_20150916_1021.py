# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmware', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vcenter',
            old_name='last_modified',
            new_name='date_modified',
        ),
    ]
