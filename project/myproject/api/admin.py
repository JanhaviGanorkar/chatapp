from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "first_name", "last_name", "is_staff", "is_superuser")  # Show first/last name
    search_fields = ("email", "first_name", "last_name")  # Allow search by name
    ordering = ("email",)  # Order by email

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

    # Ensure Django uses email instead of username
    def get_fieldsets(self, request, obj=None):
        return self.add_fieldsets if not obj else super().get_fieldsets(request, obj)

# Register the User model with the updated admin
admin.site.register(User, CustomUserAdmin)

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city"]
