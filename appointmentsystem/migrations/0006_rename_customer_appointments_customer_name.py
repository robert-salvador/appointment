# Generated by Django 4.2.3 on 2023-07-16 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0005_rename_name_timesched_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointments", old_name="customer", new_name="customer_name",
        ),
    ]
