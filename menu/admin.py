from django.contrib import admin
from .models import Category, MenuItem

# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description")
