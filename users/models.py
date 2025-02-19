from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class UserManager(BaseUserManager):
    """ Custom user manager """
    def create_user(self, email, password=None, **extra_fields):
        """ Creates user """
        if not email:
            raise ValueError('The email field is reqired')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Create and save superuser with the given email """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ Custom suer model """
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
