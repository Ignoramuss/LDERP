# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170610_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageDisability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disability_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MathematicalDisability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disability_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ParentAwarenessScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awareness_score', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='languagedisabilities',
            name='student',
        ),
        migrations.RemoveField(
            model_name='mathematicaldisabilities',
            name='student',
        ),
        migrations.RenameField(
            model_name='parentawareness',
            old_name='awareness_type',
            new_name='awareness_name',
        ),
        migrations.RemoveField(
            model_name='parentawareness',
            name='awareness_score',
        ),
        migrations.RemoveField(
            model_name='parentawareness',
            name='student',
        ),
        migrations.DeleteModel(
            name='LanguageDisabilities',
        ),
        migrations.DeleteModel(
            name='MathematicalDisabilities',
        ),
        migrations.AddField(
            model_name='parentawarenessscore',
            name='awareness_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ParentAwareness'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='language_disabilities',
            field=models.ManyToManyField(to='login.LanguageDisability'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='mathematical_disabilities',
            field=models.ManyToManyField(to='login.MathematicalDisability'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='parent_awareness_scores',
            field=models.ManyToManyField(to='login.ParentAwarenessScore'),
        ),
    ]
