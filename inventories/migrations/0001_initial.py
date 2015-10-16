# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('variables', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('ipAddress', models.GenericIPAddressField(null=True)),
                ('port', models.PositiveIntegerField(null=True)),
                ('hostKey', models.TextField(null=True)),
                ('privateKey', models.TextField(null=True)),
                ('publicKey', models.TextField(null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('variables', models.TextField(null=True, blank=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('group', models.ManyToManyField(to='inventories.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='Inventories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('variables', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='hosts',
            name='inventory',
            field=models.ManyToManyField(to='inventories.Inventories'),
        ),
        migrations.AddField(
            model_name='groups',
            name='inventory',
            field=models.ManyToManyField(to='inventories.Inventories'),
        ),
    ]
