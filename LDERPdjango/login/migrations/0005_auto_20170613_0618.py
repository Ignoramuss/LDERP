# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170613_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='parent_awareness_scores',
        ),
        migrations.AddField(
            model_name='parentawarenessscore',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.StudentInfo'),
        ),
    ]
