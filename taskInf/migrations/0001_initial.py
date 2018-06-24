# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=128, verbose_name='taskName')),
                ('taskFrequency', models.IntegerField(choices=[(0, '\u4e00\u6b21\u6027'), (1, '\u5468\u671f\u6027')], default=0, verbose_name='taskFrequency')),
                ('taskType', models.IntegerField(choices=[(0, '\u6295\u7968'), (1, '\u53cd\u9988\u4fe1\u606f'), (2, '\u63d0\u9192')], default=2, verbose_name='taskType')),
                ('taskCreateTime', models.DateTimeField(auto_now_add=True, verbose_name='taskCreateTime')),
                ('taskLastModifyTime', models.DateTimeField(auto_now=True, verbose_name='taskLastModifyTime')),
            ],
            options={
                'db_table': 'nn_task',
            },
        ),
        migrations.CreateModel(
            name='TaskOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionIDRelative', models.IntegerField(verbose_name='optionIDRelative')),
                ('optionName', models.CharField(max_length=128, verbose_name='optionName')),
                ('optionValue', models.CharField(max_length=512, verbose_name='optionValue')),
                ('optionOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskInf.GenericTask')),
            ],
            options={
                'db_table': 'nn_option',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=128, verbose_name='userName')),
                ('userNickName', models.CharField(max_length=128, verbose_name='userNickName')),
            ],
            options={
                'db_table': 'nn_user',
            },
        ),
        migrations.AddField(
            model_name='generictask',
            name='taskOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskInf.User'),
        ),
    ]
