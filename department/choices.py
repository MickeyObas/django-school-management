from .models import Department


DEPARTMENT_CHOICES = [
    (dept.abbreviation, dept.name) for dept in Department.objects.all()
]
