from django.contrib import admin

from .models import Message, MessageNotififcation


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "recipient", "title", "timestamp"]
    list_display_links = ["sender", "recipient"]
    list_filter = ["sender"]


@admin.register(MessageNotififcation)
class MessageNotificationAdmin(admin.ModelAdmin):
    list_display = ["recipient", "is_read"]
