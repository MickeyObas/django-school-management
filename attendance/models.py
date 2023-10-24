from django.db import models
from django.utils import timezone

from profiles.models import Student, Lecturer


class StudentAttendance(models.Model):
    class Status(models.TextChoices):

        PRESENT = "P", "Present"
        ABSENT = "A", "Absent"

    class Meta:
        verbose_name = "StudentAttendance item"
        verbose_name_plural = "StudentAttendance items"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # FIXME: Keep attendance record even after student gets deleted.
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=Status.choices)
    comment = models.TextField(max_length=256, blank=True, null=True)

    def __str__(self):

        return (
            f"{self.student.first_name} was {self.get_status_display()} on {self.date}"
        )
