from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# NOTE: I should probably port to lazy relationship if a circular import error occurs.
from curriculum.models import Course
from profiles.models import Student


class CourseGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    c_a_total = models.PositiveSmallIntegerField('CA total', validators=[MaxValueValidator(40, "Continuous Assessment total cannot be more than 40 marks.")], default=0)
    exam_total = models.PositiveSmallIntegerField(validators=[MaxValueValidator(60,  "Exam total cannot be more than 60 marks.")], default=0)
    approved = models.BooleanField(default=False)
    is_default = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Course Grade'
        verbose_name_plural = 'Course Grades'
        ordering = ['student__matric_number']

    @property
    def overall(self):
        return self.c_a_total + self.exam_total
    
    @property
    def grade_letter(self):
        if 70 <= self.overall <= 100:
            return 'A'
        elif 60 <= self.overall <= 69:
            return 'B'
        elif 50 <= self.overall <= 59:
            return 'C'
        elif 45 <= self.overall <= 49:
            return 'D'
        elif 0 <= self.overall <= 44:
            return 'F'
        else:
            return "Invalid Score"

    
    # NOTE For admin display purposes only
    @property
    def student_matric_number(self):
        return f"{self.student.matric_number}"
    
    def __str__(self):
        return f"{self.student.matric_number}: {self.overall} marks"


