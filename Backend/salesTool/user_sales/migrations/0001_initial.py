# Generated by Django 5.0.4 on 2024-05-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SalesUser",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("contact_number", models.CharField(max_length=15)),
                ("address1", models.CharField(max_length=255)),
                ("access_level", models.CharField(max_length=50)),
                ("number_of_sales", models.IntegerField(default=0)),
            ],
        ),
    ]
