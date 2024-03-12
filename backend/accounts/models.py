from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager

# User Model은 AbstractUser를 상속
class User(AbstractUser): 
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=10, unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    first_name = None
    last_name = None

    def __str__(self):
        return self.email