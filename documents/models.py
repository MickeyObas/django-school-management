from django.db import models

from curriculum.models import Course


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents")

    class Meta:
        abstract = True


class CourseDocument(Document):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def _str__(self):
        return f"Course document for {self.course.title}"
