from django.db import models
from django.urls import reverse

from profiles.models import Student


class Course(models.Model):
    no_of_units = models.IntegerField(default=2)
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70)
    synopsis = models.TextField(null=True)

    # TODO Create Document model that can hold documents (mostly PDFS). This field can hold study material, student scores or memos. Research the best way to handle such functionality. These documents can either be user-uploaded, staff-uploaded or admin-uploaded.

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


class DepartmentLevelCoursePack(models.Model):
    department = models.ForeignKey(
        "department.Department", on_delete=models.SET_NULL, null=True
    )
    level = models.CharField(max_length=3)
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = "DepartmentLevelCoursePack"
        verbose_name_plural = "DepartmentLevelCoursePacks"

    def __str__(self):
        return (
            f"Course pack for {self.level} level {self.department} department students"
        )
