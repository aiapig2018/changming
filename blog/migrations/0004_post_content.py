# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-02 09:46
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180201_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='详情介绍'),
        ),
    ]
