# Generated by Django 4.2.5 on 2023-10-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0028_remove_lecturer_email_remove_student_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture746", max_length=256),
        ),
    ]