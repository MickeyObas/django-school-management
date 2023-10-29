from django.core.management.base import BaseCommand

from ...models import CourseGrade
from profiles.models import Student
from curriculum.models import Course

import random

class Command(BaseCommand):
    help = "Populate student scores with random scores"

    def handle(self, *args, **kwargs):

        CA_MAX = 40
        EXAM_MAX = 60
            
        for student in Student.objects.all():
            for course in student.course_pack.courses.all():
                try:
                    course_grade = CourseGrade.objects.get(student=student, course=course)
                except:
                    course_grade = CourseGrade.objects.create(student=student, course=course)
                    course_grade.c_a_total = random.randint(1, CA_MAX)
                    course_grade.exam_total = random.randint(1, EXAM_MAX)
                    course_grade.save()
        
        self.stdout.write(self.style.SUCCESS("Successfully populated scores."))

            




