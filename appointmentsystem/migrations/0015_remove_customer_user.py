# Generated by Django 4.2.3 on 2023-07-24 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0014_alter_customer_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="customer", name="user",),
    ]
