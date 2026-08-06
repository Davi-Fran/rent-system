from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Property, Agreement, Payment

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Dados do sistema de aluguéis",
            {
                "fields": (
                    "telephone",
                    "user_type",
                )
            }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Dados do sistema de aluguéis",
            {
                "fields": (
                    "email",
                    "telephone",
                    "user_type",
                )
            }
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "is_staff",
        "is_active",
        "telephone"
    )

    list_filter = (
        "user_type",
        "is_staff",
        "is_active",
    )

admin.site.register(Property)
admin.site.register(Agreement)
admin.site.register(Payment)
