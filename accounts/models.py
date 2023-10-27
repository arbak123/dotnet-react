from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Account(AbstractBaseUser):
    """
    Custom user model representing an account in the system,
    extending AbstractBaseUser to allow customized authentication 
    using email as the unique identifier.

    Additional attributes include basic personal information, account status,
    and timestamps for user registration and last login.

    The __str__ method returns the user's email address.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # defect atributes from django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'usename', 'first_name',
        'last_name'

    ]

    def __str__(self) -> str:
        return self.email
