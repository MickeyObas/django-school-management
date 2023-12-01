from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save

from .models import Student
from curriculum.models import DepartmentLevelCoursePack


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
