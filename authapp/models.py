from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_profile', **NULLABLE, verbose_name='Avatar'),
    age = models.PositiveIntegerField(verbose_name='Age', **NULLABLE)
