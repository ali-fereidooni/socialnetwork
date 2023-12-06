from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number', 'full_name']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin


class Relation(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followings')
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} is following {self.to_user}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(null=True, blank=True)
