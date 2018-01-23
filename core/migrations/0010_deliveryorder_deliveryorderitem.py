# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_itemgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_number', models.CharField(blank=True, max_length=30, null=True)),
                ('do_customer', models.CharField(blank=True, max_length=30, null=True)),
                ('do_reference', models.CharField(blank=True, max_length=30, null=True)),
                ('do_date', models.CharField(blank=True, max_length=30, null=True)),
                ('do_qty_total', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_number', models.CharField(blank=True, max_length=30, null=True)),
                ('do_item_id', models.CharField(blank=True, max_length=30, null=True)),
                ('do_item_qty', models.CharField(blank=True, max_length=30, null=True)),
                ('do_item_rate', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
