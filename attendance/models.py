from django.db import models
from django.utils import timezone

from profiles.models import Student, Lecturer


class StudentAttendance(models.Model):
    class Status(models.TextChoices):

        PRESENT = "P", "Present"
        ABSENT = "A", "Absent"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # FIXME: Keep attendance record even after student gets deleted.
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=1, choices=Status.choices)
    comment = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'date'], name="one-attendance-per-date")
        ]
        verbose_name = "StudentAttendance item"
        verbose_name_plural = "StudentAttendance items"

    def __str__(self):

        return (
            f"{self.student.user.first_name} was {self.get_status_display()} on {self.date}"
        )
