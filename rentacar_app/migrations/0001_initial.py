# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('plate', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('price_per_day', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField()),
                ('predicted_delivery_date', models.DateField()),
                ('real_delivery_date', models.DateField(blank=True)),
                ('total_price', models.FloatField(blank=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rentacar_app.Car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rentacar_app.Customer')),
            ],
        ),
    ]
