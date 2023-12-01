from django.contrib import admin

from .models import *


@admin.register(CourseDocument)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["title", "file"]
