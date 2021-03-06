# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-22 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0148_auto_20190222_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internselection',
            name='final_feedback_due',
            field=models.DateField(blank=True, verbose_name='Date final feedback form due (typically 3 days after the internship ends)'),
        ),
        migrations.AlterField(
            model_name='internselection',
            name='final_feedback_opens',
            field=models.DateField(blank=True, verbose_name='Date final feedback form opens'),
        ),
    ]
