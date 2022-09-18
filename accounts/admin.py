from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile, TeacherProfile
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['email', 'account_type', 'date_joined']
    list_display_links = ['email']

    fieldsets = (
        ('Credentials', {'fields':('email', 'password',)}),
        ('Permissions', {'fields':('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_type', 'email', 'password1', 'password2')
        }),
    )

    ordering = ['email']

admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)