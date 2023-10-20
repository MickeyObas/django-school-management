# Generated by Django 4.2.5 on 2023-10-17 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0014_alter_lecturer_courses_taught_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="date_of_hire",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 17, 15, 55, 17, 143409, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture790", max_length=256),
        ),
    ]