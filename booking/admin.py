from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "datetime", "people", "created_at")
    list_filter = ("datetime", "created_at")
    search_fields = ("name", "email", "special_requests")
    ordering = ("-created_at",)
