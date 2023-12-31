# Generated by Django 4.2.3 on 2023-07-27 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0039_appointmentnew_chosen_barber"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointmentnew",
            name="additional_drink",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="appointmentsystem.beverage",
            ),
        ),
    ]
