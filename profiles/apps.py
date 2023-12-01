from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    def ready(self) -> None:

        from .signals import assign_course_pack_to_student
        from accounts.signals import create_profile_from_user

        return super().ready()
