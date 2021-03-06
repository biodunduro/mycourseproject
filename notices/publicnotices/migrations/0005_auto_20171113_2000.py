# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicnotices', '0004_publicnotice_medium'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='post/images')),
            ],
        ),
        migrations.AddField(
            model_name='medium',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicnotice',
            name='image',
            field=models.ManyToManyField(to='publicnotices.PostImage'),
        ),
    ]
