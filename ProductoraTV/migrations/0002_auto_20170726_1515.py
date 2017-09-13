# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-07-26 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductoraTV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=13)),
                ('correo', models.CharField(max_length=200)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=9)),
                ('celular', models.CharField(max_length=14)),
                ('genero', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]