from django.db import models
from django.urls import reverse

class Course(models.Model):
    no_of_units = models.IntegerField(default=2)
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70)

    # TODO Create Document model that can hold documents (mostly PDFS). This field can hold study material, student scores or memos. Research the best way to handle such functionality. These documents can either be user-uploaded, staff-uploaded or admin-uploaded.

    def __str__(self):
        return self.code
    
    def get_absolute_url(self):
        return reverse('course_page', kwargs={'course_slug': self.slug})
    
    def get_assigned_lecturers(self):
        pass

class DepartmentLevelCoursePack(models.Model):
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=3)
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = 'DepartmentLevelCoursePack'
        verbose_name_plural = 'DepartmentLevelCoursePacks'

    def __str__(self):
        return f"Course pack for {self.level} level {self.department} department students"
