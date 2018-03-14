from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=32, verbose_name="Phone", name="phone", blank=True, null=True)
    occupation_field = models.CharField(max_length=32, verbose_name="Occupation Field", name="occupation_field", blank=True, null=True)
    occupation = models.CharField(max_length=32, verbose_name="Occupation", name="occupation", blank=True, null=True)
    birthdate = models.DateField(verbose_name="Birth Date", name="birthdate", auto_now_add=False, auto_now=False, blank=True, null=True)
    description = models.TextField(verbose_name="Description", name="description", blank=True, null=True)

    def __str__(self):
        return self.username
