# Generated by Django 4.2.3 on 2023-07-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="barber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="beverage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("price", models.FloatField(null=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Alcoholic", "Alcoholic"),
                            ("Non - Alcoholic", "Non - Alcoholic"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("description", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="complementarydrink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("price", models.FloatField(null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="timesched",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
