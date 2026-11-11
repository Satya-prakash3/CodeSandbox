
from django.utils import timezone
from django.core.validators import validate_email
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def get_by_natural_key(self, email):
        email = self.normalize_email(email).lower()
        

        return self.get(
            **{self.model.USERNAME_FIELD: email}
        )

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")

        email = self.normalize_email(email).lower()
        email = validate_email(email)

        extra_fields.setdefault("is_active", False)

        user = self.model(
            email=email,
            **extra_fields,
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise ValueError("Superuser must have a password.")

        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields["is_active"] = True

        if not extra_fields.get("email_verified_at"):
            extra_fields["email_verified_at"] = timezone.now()

        return self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
