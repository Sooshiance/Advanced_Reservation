from django.contrib import admin

from .models import Item, Cart, Order


@admin.register(Item)
class OAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']


@admin.register(Cart)
class CAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'peak']


@admin.register(Order)
class OAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_user_role', 'cart']
