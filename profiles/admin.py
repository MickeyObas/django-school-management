from django.contrib import admin

from .models import Student, Lecturer

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'last_name', 'first_name', 'gender', 'level', 'department']
    list_display_links = ['user']
    search_fields = ['last_name']

admin.site.register(Lecturer)


