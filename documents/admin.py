from django.contrib import admin

from .models import *
from core.admin import custom_admin_site


class CourseDocumentAdmin(admin.ModelAdmin):
    list_display = ["title", "file", "course"]


custom_admin_site.register(CourseDocument, CourseDocumentAdmin)
