from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    address = models.TextField(max_length=500, blank=False)