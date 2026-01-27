from django.contrib.auth.models import AbstractUser, UserManager,BaseUserManager
from django.core.validators import RegexValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)

        if password:
            user.set_password(password)
        else:
            raise ValueError("Users must have a password")
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        print(extra_fields)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_renter", True)

        if (extra_fields.get("is_staff") is not True or
            extra_fields.get("is_superuser") is not True or
            extra_fields.get("is_active") is not True or
            extra_fields.get("is_renter") is not True):
            raise TypeError("Superuser must have is_staff, is_superuser, is_active, is_renter")
        return self.create_user(email, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractUser):
    pfone_regex_code = RegexValidator(
        regex=r'^(\+351|\(\+351\))?9\d{8}$',
        message="Enter a valid PT number in next format (+351)999999999 or +351999999999 or 999999999"
    )

    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_renter = models.BooleanField(default=False)
    phone = models.CharField(validators=[pfone_regex_code], max_length=14, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
