from django.contrib import admin

from .models import PaymentReceipt, PaymentRecord, PaymentType


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "level"]


admin.site.register(PaymentReceipt)
admin.site.register(PaymentRecord)
