# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20170911_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='github_link',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
