from django.contrib import admin

from .models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
