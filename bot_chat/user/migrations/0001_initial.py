# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-08-03 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonCall',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_button_name', models.CharField(max_length=150)),
                ('int_count', models.IntegerField()),
                ('dat_created', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_ptr_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_user_name', models.CharField(max_length=150)),
                ('int_count', models.IntegerField()),
                ('dat_joined', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
