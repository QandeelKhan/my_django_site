# Generated by Django 3.1.4 on 2020-12-23 22:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201224_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 22, 40, 31, 56987, tzinfo=utc)),
        ),
    ]
