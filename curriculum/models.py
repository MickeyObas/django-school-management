from django.db import models

class Course(models.Model):
    # TODO Enrich this class with fields such as no. of units.
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_assigned_lecturers(self):
        pass