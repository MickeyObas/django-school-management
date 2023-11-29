import uuid

from django.db import models

from accounts.models import User


class PaymentType(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    level = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title


class PaymentRecord(models.Model):

    STATUS_CHOICES = (
        ('A', 'Approved'),
        ('P', 'Pending'),
        ('R', 'Rejected'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    payment_type = models.OneToOneField('PaymentType', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        f"{self.payer}: {self.payment_type.title}: {self.status}"


class PaymentReceipt(models.Model):
    payment_record = models.OneToOneField('PaymentRecord', on_delete=models.PROTECT)

    def __str__(self):
        f"Receipt for {self.payment_record.payment_type.title} by {self.payment_record.payer}"