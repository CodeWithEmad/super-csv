# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-22 06:52


import django.utils.timezone
import model_utils.fields
from django.db import migrations, models

import super_csv.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('class_name', models.CharField(db_index=True, max_length=255)),
                ('unique_id', models.CharField(db_index=True, max_length=255)),
                ('operation', models.CharField(max_length=255)),
                ('data', models.FileField(max_length=255, upload_to=super_csv.models.csv_class_path)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
