# Generated by Django 4.1 on 2022-09-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_studentprofile_options_teacherprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='school_grade',
            field=models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SS1', 'SS1'), ('SS2', 'SS2'), ('SS3', 'SS3')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='school_grade',
            field=models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SS1', 'SS1'), ('SS2', 'SS2'), ('SS3', 'SS3')], max_length=4, null=True),
        ),
    ]
