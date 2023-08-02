# Generated by Django 4.2.3 on 2023-07-28 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0046_alter_appointment_additional_drink"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="additional_drink",
            field=models.ManyToManyField(
                blank=True,
                related_name="appointment_additional_drinks",
                to="appointmentsystem.beverage",
            ),
        ),
        migrations.AlterField(
            model_name="appointmentnew",
            name="additional_drinks",
            field=models.ManyToManyField(blank=True, to="appointmentsystem.beverage"),
        ),
    ]
