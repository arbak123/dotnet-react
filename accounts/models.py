from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):
    """
    A custom manager for the Account model that provides helper
    methods for creating users and superusers.
    """
    def create_user(
        self, first_name, last_name,
        email, username, password=None
    ):
        """
        Create and return a user with the given first name,
        last name, email, username, and password.

        Raises:
        -------
        ValueError:
            If the email or username is not provided.

        Returns:
        --------
        Account:
            The created user account.
        """
        if not email:
            raise ValueError('user must have an email')

        if not username:
            raise ValueError('user must hace an username')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name, last_name,
        email, username, password
    ):
        """
        Create and return a superuser with the given first name,
        last name, email, username, and password.

        A superuser has all the permissions set to True by default.

        Returns:
        --------
        Account:
            The created superuser account.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save()
        return user


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
    email = models.EmailField(max_length=100, unique=True)
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
        'username', 'first_name',
        'last_name'

    ]

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, add_label):
        return True
