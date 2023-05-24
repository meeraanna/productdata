# Generated by Django 4.1.3 on 2023-05-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataModel",
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
                ("APIWELLNUMBER", models.CharField(max_length=250)),
                ("OIL", models.CharField(max_length=250)),
                ("GAS", models.CharField(max_length=250)),
                ("BRINE", models.CharField(max_length=250)),
            ],
        ),
    ]
