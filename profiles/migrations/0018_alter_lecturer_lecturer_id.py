# Generated by Django 4.2.5 on 2023-10-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0017_alter_lecturer_lecturer_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture604", max_length=256),
        ),
    ]