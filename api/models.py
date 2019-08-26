from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Company(models.Model):
    name = models.CharField (max_length=50)
    address = models.TextField(max_length=300)
    phone = models.CharField(max_length=20)

class Favourite (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    mark = models.NullBooleanField(default=True)

    class Meta:
        unique_together = (('user', 'company'),)
        index_together = (('user', 'company'),)