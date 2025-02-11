from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Student model (no changes needed)
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(default=1)
    city = models.CharField(max_length=100)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)  # ✅ Username field
    email = models.EmailField(unique=True)  # ✅ Email field
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    # Required fields for Django Admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="api_users",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="api_users_permissions",  
        blank=True
    )

    USERNAME_FIELD = "email"  # Login with email
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]  # ✅ Username required

    objects = UserManager()  # Assign custom manager

    def __str__(self):
        return self.username  # ✅ Now returns username instead of email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
