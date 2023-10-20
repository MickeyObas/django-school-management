from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from profiles.models import Student, Lecturer

@receiver(post_save, sender=User)
def create_profile_from_user(sender, instance, created, **kwargs):
    if created:
        if instance.account_type == 'S':
            Student.objects.create(user=instance)
        elif instance.account_type == 'L':
            Lecturer.objects.create(user=instance)
        else:
            pass
        



        

