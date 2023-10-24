from django.db import models

class Course(models.Model):
    no_of_units = models.IntegerField(default=2)
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_assigned_lecturers(self):
        pass