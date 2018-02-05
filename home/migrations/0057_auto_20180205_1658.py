# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-05 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_auto_20180205_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='date_merged',
            field=models.DateField(blank=True, help_text='If this contribution is still in progress, you can leave this field blank and edit it later.', null=True, verbose_name='Date contribution was accepted or merged (in YYYY-MM-DD format)'),
        ),
    ]