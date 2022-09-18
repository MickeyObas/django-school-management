from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from .managers import CustomUserManager, TeacherManager, StudentManager
from datetime import datetime


class User(AbstractBaseUser, PermissionsMixin):
    ACCOUNTS = (
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('ADMIN', 'Admin'),
    )

    email = models.EmailField(unique=True, max_length=255)
    account_type = models.CharField(max_length=8, choices=ACCOUNTS)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    base_account_type = ACCOUNTS[2][0]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.account_type:
                self.account_type = self.base_account_type
            return super().save(*args, **kwargs)



class Student(User):
    base_account_type = User.ACCOUNTS[0][0]
    
    class Meta:
        proxy = True

    students = StudentManager()


class Teacher(User):
    base_account_type = User.ACCOUNTS[1][0]
    
    class Meta:
        proxy = True

    teachers = TeacherManager()


class StudentProfile(models.Model):
    SCHOOL_GRADES = (
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
    )
      
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True)
    school_grade = models.CharField(max_length=4, choices=SCHOOL_GRADES, null=True)

    class Meta:
        verbose_name = 'Student Profile'
        verbose_name_plural= 'Student Profiles'

    def __str__(self):
        return self.user.email 


class TeacherProfile(models.Model):
    SCHOOL_GRADES = (
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
    )
      
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True)
    school_grade = models.CharField(max_length=4, choices=SCHOOL_GRADES, null=True)
    

    class Meta:
        verbose_name = 'Teacher Profile'
        verbose_name_plural= 'Teacher Profiles'

    def __str__(self):
        return self.user.email