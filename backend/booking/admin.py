from django.contrib import admin

from .models import Order


@admin.register(Order)
class OAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_pick']
