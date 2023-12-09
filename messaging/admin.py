from django.contrib import admin

from .models import Message, MessageNotififcation
from core.admin import custom_admin_site


class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "sender", "recipient", "title", "timestamp"]
    list_display_links = ["sender", "recipient"]
    search_fields = ["id", "sender__email", "recipient__email"]


class MessageNotificationAdmin(admin.ModelAdmin):
    list_display = ["recipient", "is_read"]


custom_admin_site.register(Message, MessageAdmin)
custom_admin_site.register(MessageNotififcation, MessageNotificationAdmin)
