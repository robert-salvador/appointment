# Generated by Django 4.2.3 on 2023-07-16 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="timesched", old_name="time", new_name="name",
        ),
    ]
