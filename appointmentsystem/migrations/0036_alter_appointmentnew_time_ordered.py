# Generated by Django 4.2.3 on 2023-07-27 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0035_alter_appointmentnew_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointmentnew",
            name="time_ordered",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 28, 21, 41, 44, 724507)
            ),
        ),
    ]
