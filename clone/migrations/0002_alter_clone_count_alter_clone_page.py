# Generated by Django 4.1.5 on 2023-02-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clone", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clone",
            name="count",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="clone",
            name="page",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]