# Generated by Django 4.2.3 on 2023-07-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0042_remove_appointmentnew_additional_drinks_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="appointmentnew", name="additional_drinks",),
        migrations.AddField(
            model_name="appointmentnew",
            name="additional_drinks",
            field=models.ManyToManyField(
                blank=True, null=True, to="appointmentsystem.beverage"
            ),
        ),
    ]
