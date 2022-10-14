from django.contrib import admin

# Register your models here.
from school_mgt_app.models import User
from django.contrib.auth.admin import  UserAdmin as AdminUser


@admin.register(User)
class UserAdmin(AdminUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", 'first_name', 'last_name'),
            },
        ),
    )