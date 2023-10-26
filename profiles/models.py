from django.db import models
from django.utils import timezone

from accounts.models import User
from department.models import Department

import random
from datetime import date
from PIL import Image


class BaseProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    profile_picture = models.ImageField(
        blank=True, null=True, upload_to="profile_picture"
    )
    birthdate = models.DateField(default=timezone.now)
    # TODO Clarify DEPARTMENT - LECTURER relaional logic.
    department = models.ForeignKey(
        Department, null=True, blank=True, on_delete=models.CASCADE
    )
    gender = models.CharField(max_length=8, choices=[("M", "Male"), ("F", "Female")])
    state_of_origin = models.CharField(max_length=20, default="Lagos")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            max_size = (120, 120)
            img.thumbnail(max_size)
            img.save(self.profile_picture.path)

    @property
    def age(self):
        today = timezone.now()
        return 22
        # return (today.year - self.birthdate.year -((today.day, today.month) < (self.birthdate.day, self.birthdate.month)))

    @property
    def full_name(self):
        return f"{self.user.last_name} {self.user.first_name} {self.user.middle_name}"
    

class Student(BaseProfile):
    class LevelChoices(models.TextChoices):
        FIRST_YEAR = "100", "100 Level"
        SECOND_YEAR = "200", "200 Level"
        THIRD_YEAR = "300", "300 Level"
        FOURTH_YEAR = "400", "400 Level"
        FIFTH_YEAR = "500", "500 Level"

    level = models.CharField(
        max_length=3, choices=LevelChoices.choices, default=LevelChoices.FIRST_YEAR
    )
    
    course_pack = models.ForeignKey('curriculum.DepartmentLevelCoursePack', on_delete=models.SET_NULL, null=True)


class Lecturer(BaseProfile):
    # TODO Add qualifications as a field.
    prefix = models.CharField(max_length=10, default='Prof')
    lecturer_id = models.CharField(
        max_length=256, default=f"lecture{random.randint(100, 1000)}"
    )
    date_of_hire = models.DateTimeField(default=timezone.now)
    teaching_experience = models.IntegerField(default=4)
    courses_taught = models.ManyToManyField('curriculum.Course', blank=True)

    def __str__(self):
        if not self.prefix:
            return super().__str__()
        else:
            return f"{self.prefix}. {self.user.last_name} {self.user.first_name}"
# TODO Write script to bulk create users and profiles.
