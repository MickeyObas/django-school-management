from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # TODO A lecturer should only be the HOD of a department they're registered under.
    head_of_department = models.OneToOneField(
        "profiles.Lecturer",
        on_delete=models.DO_NOTHING,
        related_name="dept_in_charge_of",
        blank=True,
        null=True,
    )
    description = models.TextField()
    location = models.CharField(max_length=256)
    logo = models.ImageField(blank=True, null=True)
    abbreviation = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.abbreviation

    @property
    def faculty_members(self):
        return self.lecturer_set.all()

    @property
    def enrolled_students(self):
        return self.student_set.all()

    @property
    def no_of_enrolled_students(self):
        return self.student_set.all().count()

    @property
    def no_of_enrolled_staff(self):
        return self.lecturer_set.all().count()


class CourseRegistrationOfficer(models.Model):
    class LevelChoices(models.TextChoices):
        FIRST_YEAR = "100", "100 Level"
        SECOND_YEAR = "200", "200 Level"
        THIRD_YEAR = "300", "300 Level"
        FOURTH_YEAR = "400", "400 Level"
        FIFTH_YEAR = "500", "500 Level"

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=3, choices=LevelChoices.choices)
    lecturer = models.ForeignKey("profiles.Lecturer", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Course Registration Officer"
        verbose_name_plural = "Course Registration Officers"
        constraints = [
            models.UniqueConstraint(
                fields=["department", "lecturer", "level"],
                name="one-officer-per-department-level",
            )
        ]
