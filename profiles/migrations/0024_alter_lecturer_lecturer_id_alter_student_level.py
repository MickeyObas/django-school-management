# Generated by Django 4.2.5 on 2023-10-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0023_alter_lecturer_lecturer_id_alter_student_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture934", max_length=256),
        ),
        migrations.AlterField(
            model_name="student",
            name="level",
            field=models.CharField(
                choices=[
                    ("100", "100 Level"),
                    ("200", "200 Level"),
                    ("300", "300 Level"),
                    ("400", "400 Level"),
                    ("500", "500 Level"),
                ],
                default="100",
                max_length=3,
            ),
        ),
    ]