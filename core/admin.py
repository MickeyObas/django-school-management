from typing import Any
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from accounts.models import User
from profiles.models import Student, Lecturer


class CustomAdmiSite(admin.AdminSite):
    site_header = "Schooled-You"
    site_title = "Schooled-You Admin Site"
    # enable_nav_sidebar = False

    def get_app_list(self, request: WSGIRequest) -> list[Any]:

        new_app_order = {
            "accounts": 0,
            "profiles": 1,
            "grading": 2,
            "curriculum": 3,
            "department": 3,
            "grading": 4,
            "attendance": 5,
            "messaging": 6,
            "payments": 7,
            "documents": 8,
        }

        profiles_order = {"Students": 0, "Lecturers": 1}

        curriculum_order = {
            "Courses": 0,
            "Course(s) Outline": 1,
            "DepartmentLevelCoursePacks": 2,
        }

        app_list = super().get_app_list(request)
        app_list.sort(key=lambda app: new_app_order[app["app_label"]])

        for app in app_list:
            if app["app_label"] == "profiles":
                app["models"].sort(key=lambda model: profiles_order[model["name"]])
            if app["app_label"] == "curriculum":
                app["models"].sort(key=lambda model: curriculum_order[model["name"]])

        return app_list


custom_admin_site = CustomAdmiSite()
