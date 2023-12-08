from django.db import models
from django.urls import reverse

from profiles.models import Student


class Course(models.Model):
    no_of_units = models.IntegerField(default=2)
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70)
    synopsis = models.TextField(null=True)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("course_page", kwargs={"course_slug": self.slug})

    def get_assigned_lecturers(self):
        return self.lecturer_set.all()

    # FIXME There is definitely a less expensive way to do this lmfao, but I just did this to test things
    def get_students(self):
        students = []
        for student in Student.objects.order_by("department"):
            if student.course_pack:
                course_codes = []
                for course in student.course_pack.courses.all():
                    course_codes.append(course.code)
                if self.code in course_codes:
                    students.append(student)
            else:
                # Student hasn't been assigned a course pack yet
                pass

        return students

    @property
    def course_code_prefix(self):
        prefix = ''
        for char in self.code:
            if char.isalpha():
                prefix += char
            else:
                break
        return prefix



class CourseScheme(models.Model):
    course = models.OneToOneField("Course", on_delete=models.CASCADE)
    week_1 = models.CharField(max_length=120, null=True, blank=True)
    week_2 = models.CharField(max_length=120, null=True, blank=True)
    week_3 = models.CharField(max_length=120, null=True, blank=True)
    week_4 = models.CharField(max_length=120, null=True, blank=True)
    week_5 = models.CharField(max_length=120, null=True, blank=True)
    week_6 = models.CharField(max_length=120, null=True, blank=True)
    week_7 = models.CharField(max_length=120, null=True, blank=True)
    week_8 = models.CharField(max_length=120, null=True, blank=True)
    week_9 = models.CharField(max_length=120, null=True, blank=True)
    week_10 = models.CharField(max_length=120, null=True, blank=True)
    week_11 = models.CharField(max_length=120, null=True, blank=True)
    week_12 = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Course(s) Outline"

    def __str__(self):
        return f"Course scheme/outline for {self.course.code}"


class DepartmentLevelCoursePack(models.Model):
    department = models.ForeignKey(
        "department.Department", on_delete=models.SET_NULL, null=True
    )
    level = models.CharField(max_length=3)
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = "DepartmentLevelCoursePack"
        verbose_name_plural = "DepartmentLevelCoursePacks"

    def total_no_of_units(self):
        total = 0
        if self.courses:
            for course in self.courses.all():
                total += course.no_of_units
        return total

    def __str__(self):
        return (
            f"{self.department.abbreviation} - {self.level}"
        )
