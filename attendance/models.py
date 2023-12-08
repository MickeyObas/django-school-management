from django.db import models
from django.utils import timezone

from profiles.models import Student, Lecturer
from curriculum.models import Course


class StudentAttendance(models.Model):
    class Status(models.TextChoices):

        PRESENT = "P", "Present"
        ABSENT = "A", "Absent"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # FIXME: Keep attendance record even after student gets deleted.
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=1, choices=Status.choices)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=2)
    comment = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "date", "course"], name="one-attendance-per-date"
            )
        ]
        verbose_name = "StudentAttendance Item"
        verbose_name_plural = "StudentAttendance Items"

    @property
    def matric_number(self):
        return self.student.matric_number

    def __str__(self):

        return f"{self.matric_number}: {self.student.user.last_name} {self.student.user.first_name} was {self.get_status_display()} on {self.date}"
