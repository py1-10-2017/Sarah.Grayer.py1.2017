# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas.dojo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]