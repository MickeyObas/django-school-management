# Generated by Django 4.2.5 on 2023-10-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0024_alter_lecturer_lecturer_id_alter_student_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture606", max_length=256),
        ),
    ]
