# Generated by Django 4.0.4 on 2022-11-30 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0055_add_voucher_add_voucher2_add_voucher3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_itemcreation',
            name='under',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app1.createstockgrp'),
        ),
    ]
