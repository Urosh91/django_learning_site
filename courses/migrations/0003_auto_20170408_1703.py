# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_step'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['-order']},
        ),
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
