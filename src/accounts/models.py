import uuid
from django.db import models
from django.db.models.functions import Lower
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin
)

from accounts.managers import CustomUserManager
from common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid7,
        editable=False
    )
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    email_verified_at = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    username = None

    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = []  

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("email"),
                name="unique_lowercase_email"
            )
        ]
        db_table = "accounts_user"

    def __str__(self):
        return self.email
    

class UserProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )
    display_name = models.CharField(
        max_length=100,
        blank=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True
    )

