# Generated by Django 4.2.3 on 2023-07-16 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0003_appointments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointments",
            name="additional_drink",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="appointmentsystem.beverage",
            ),
        ),
        migrations.AlterField(
            model_name="appointments",
            name="corresponding_drink",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="appointmentsystem.complementarydrink",
            ),
        ),
    ]
