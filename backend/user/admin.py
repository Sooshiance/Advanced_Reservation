from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile, OTP


class Admin(UserAdmin):
    list_display = ('phone', 'email', 'is_active', 'pk', 'role')
    filter_horizontal = ()
    list_filter = ('role', 'is_active')
    fieldsets = ()
    search_fields = ('email', 'phone')
    list_display_links = ('phone', 'email')
    # This line below added because 'ordering' attribute need a dependency
    ordering = ('email',)


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'email', 'pk']
    search_fields = ('phone', 'user')
    sortable_by = ('pk', 'user')


class OTPAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp']


admin.site.register(User, Admin)

admin.site.register(Profile, AdminProfile)

admin.site.register(OTP, OTPAdmin)
