from django.contrib import admin

from .models import Course, DepartmentLevelCoursePack

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'title']
    prepopulated_fields = {'slug': ('code','title',)}
    
@admin.register(DepartmentLevelCoursePack)
class DepartmentLevelCoursePackAdmin(admin.ModelAdmin):
    list_display = ['department', 'level']
    
    


