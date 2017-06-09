# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-09 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='language_disabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='mathematical_disabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='parent_awareness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awareness_type', models.CharField(max_length=200)),
                ('awareness_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=200)),
                ('stud_school', models.CharField(max_length=200)),
                ('stud_standard', models.CharField(max_length=30)),
                ('stud_div', models.CharField(max_length=30)),
                ('date_of_fill', models.DateField()),
                ('date_of_birth', models.DateField()),
                ('father_name', models.CharField(max_length=200)),
                ('father_contact', models.BigIntegerField()),
                ('father_email', models.EmailField(max_length=200)),
                ('father_education', models.CharField(max_length=200)),
                ('father_occupation', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('mother_contact', models.BigIntegerField()),
                ('mother_email', models.EmailField(max_length=200)),
                ('mother_education', models.CharField(max_length=200)),
                ('mother_occupation', models.CharField(max_length=200)),
                ('stud_grades', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='parent_awareness',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Student_info'),
        ),
        migrations.AddField(
            model_name='mathematical_disabilities',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Student_info'),
        ),
        migrations.AddField(
            model_name='language_disabilities',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Student_info'),
        ),
    ]