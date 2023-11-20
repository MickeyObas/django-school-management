from django.db import models

from accounts.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_received"
    )
    title = models.CharField(max_length=35)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)

    class Meta:
        ordering = ["-is_favourite", "-timestamp",]

    def __str__(self):
        return f"Message by {self.sender.email} to {self.recipient.email}"


class MessageNotififcation(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Message Notification"
        verbose_name_plural = "Message Notifications"
