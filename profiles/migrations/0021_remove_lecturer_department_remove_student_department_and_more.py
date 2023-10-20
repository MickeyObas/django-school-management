# Generated by Django 4.2.5 on 2023-10-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0020_alter_lecturer_lecturer_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lecturer",
            name="department",
        ),
        migrations.RemoveField(
            model_name="student",
            name="department",
        ),
        migrations.AlterField(
            model_name="lecturer",
            name="lecturer_id",
            field=models.CharField(default="lecture576", max_length=256),
        ),
    ]