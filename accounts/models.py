from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from .managers import CustomUserManager, TeacherManager, StudentManager
from datetime import datetime


class User(AbstractBaseUser, PermissionsMixin):
    class AccountChoices(models.TextChoices):
        STUDENT = 'S', 'Student'
        LECTURER = 'L', "Lecturer"

    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    account_type = models.CharField(max_length=1, choices=AccountChoices.choices, default='S')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_login = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

