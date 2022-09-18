from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User, Student, TeacherProfile, StudentProfile


@receiver(post_save, sender=User)
def assign_group_create_profile(sender, instance, created, **kwargs):
    if created and instance.account_type == 'STUDENT':
        StudentProfile.objects.create(user=instance)
        student_group, was_created = Group.objects.get_or_create(name='Student')
        instance.groups.add(student_group)
    elif created and instance.account_type == 'TEACHER':
        TeacherProfile.objects.create(user=instance)
        teacher_group, was_created = Group.objects.get_or_create(name='Teacher')
        instance.groups.add(teacher_group)
    else:
        if created and instance.account_type == 'ADMIN':
            admin_group, was_created = Group.objects.get_or_create(name='Admin')
        

