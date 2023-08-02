# Generated by Django 4.2.3 on 2023-07-27 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0034_alter_appointmentnew_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointmentnew",
            name="time",
            field=models.CharField(
                choices=[
                    ("9 AM", "9 AM"),
                    ("10 AM", "10 AM"),
                    ("11 AM", "11 AM"),
                    ("12 PM", "12 PM"),
                    ("1 PM", "1 PM"),
                    ("2 PM", "2 PM"),
                    ("3 PM", "3 PM"),
                    ("4 PM", "4 PM"),
                    ("5 PM", "5 PM"),
                    ("6 PM", "6 PM"),
                    ("7 PM", "7 PM"),
                ],
                default="9 AM",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="appointmentnew",
            name="time_ordered",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 30, 21, 40, 13, 374911)
            ),
        ),
    ]