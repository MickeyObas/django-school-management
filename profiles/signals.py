from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save

from .models import Student
from curriculum.models import DepartmentLevelCoursePack

from random import randint
from datetime import datetime


@receiver(post_save, sender=Student)
def assign_matric_number_to_student(sender, instance, created, **kwargs):
    if not created and not instance.matric_number and instance.department is not None:
        student_department = instance.department
        current_year = datetime.now().strftime("%y")
        student_matric_number = f"{student_department.abbreviation}/{current_year}/{randint(1000, 9999)}"
        Student.objects.filter(id=instance.id).update(matric_number=student_matric_number)


@receiver(post_save, sender=Student)
def assign_course_pack_to_student(sender, instance, created, **kwargs):
    if not created:
        if not instance.user.first_login and instance.department is not None:
            department = instance.department
            level = instance.level
            required_department_level_course_pack = get_object_or_404(
                DepartmentLevelCoursePack, department=department, level=level
            )
            Student.objects.filter(id=instance.id).update(
                course_pack=required_department_level_course_pack
            )

