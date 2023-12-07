from django.contrib import admin

from core.admin import custom_admin_site
from .models import PaymentReceipt, PaymentRecord, PaymentType


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "level"]


custom_admin_site.register(PaymentReceipt)
custom_admin_site.register(PaymentRecord)
custom_admin_site.register(PaymentType, PaymentTypeAdmin)
