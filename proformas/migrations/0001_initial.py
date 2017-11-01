# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-12 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=50)),
                ('tipo_proformas', models.CharField(choices=[('S_I', 's_individuales'), ('R_S', 'r_servicios'), ('P_S', 'p_servicios')], max_length=3)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]