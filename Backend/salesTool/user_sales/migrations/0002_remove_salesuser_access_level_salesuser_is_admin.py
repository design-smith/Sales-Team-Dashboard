# Generated by Django 5.0.4 on 2024-05-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_sales", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salesuser",
            name="access_level",
        ),
        migrations.AddField(
            model_name="salesuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
