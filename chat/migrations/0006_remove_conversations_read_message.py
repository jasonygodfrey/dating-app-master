# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-05 23:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_messages_conversation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversations',
            name='read_message',
        ),
    ]