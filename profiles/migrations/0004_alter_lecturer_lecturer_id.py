# Generated by Django 4.2.5 on 2023-10-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_student_created_student_level_student_updated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture958", max_length=256),
        ),
    ]