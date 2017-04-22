# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='id',
            new_name='item_id',
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('S', 'story'), ('C', 'comment')], max_length=10),
        ),
    ]
