# Generated by Django 4.2.3 on 2023-07-26 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0021_alter_timeschedule_date"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="timeschedule", unique_together={("date", "time")},
        ),
    ]
