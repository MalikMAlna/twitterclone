from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class TwitterUserManager(UserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must provide an email address!")
        if not username:
            raise ValueError("Users must provide a username!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError("Superusers must provide an email address!")
        if not username:
            raise ValueError("Superusers must provide a username!")

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class TwitterUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True)

    objects = TwitterUserManager()

    def __str__(self):
        return self.username
