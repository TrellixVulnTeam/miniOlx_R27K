# Generated by Django 2.1.1 on 2018-12-26 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20181227_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 27, 1, 18, 7, 6946)),
        ),
    ]