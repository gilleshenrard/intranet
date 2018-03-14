from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=32, verbose_name="Country of origin", name="country", blank=True, null=True)
    phone = models.CharField(max_length=32, verbose_name="Phone", name="phone", blank=True, null=True)
    field = models.CharField(max_length=32, verbose_name="Field of occupation", name="field", blank=True, null=True)
    occupation = models.CharField(max_length=32, verbose_name="Occupation", name="occupation", blank=True, null=True)
    birthdate = models.DateField(verbose_name="Birth Date", name="birthdate", auto_now_add=False, auto_now=False, blank=True, null=True)
    description = models.TextField(verbose_name="Description", name="description", blank=True, null=True)

    def __str__(self):
        return self.username
