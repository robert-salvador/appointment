# Generated by Django 4.2.3 on 2023-08-01 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointmentsystem", "0048_alter_appointmentnew_chosen_barber"),
    ]

    operations = [
        migrations.RemoveField(model_name="appointment", name="additional_drink",),
        migrations.RemoveField(model_name="appointment", name="chosen_barber",),
        migrations.RemoveField(model_name="appointment", name="corresponding_drink",),
        migrations.RemoveField(model_name="appointment", name="customer_name",),
        migrations.RemoveField(model_name="appointment", name="picked_service",),
        migrations.RemoveField(model_name="appointment", name="schedule",),
        migrations.DeleteModel(name="customer",),
        migrations.AlterUniqueTogether(name="timeschedule", unique_together=None,),
        migrations.RemoveField(model_name="timeschedule", name="booked_by",),
        migrations.DeleteModel(name="appointment",),
        migrations.DeleteModel(name="timeschedule",),
    ]