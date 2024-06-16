from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User, UserOTP


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'email', 'phone', 'business_name', "firstname", "lastname", "otp", "otp_verified", "country", "is_active", 'last_login', "password")}),
    )

    list_display = ("business_name", 'email', 'phone', 'is_staff', 'otp', "is_active", 'otp_verified', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(UserOTP)