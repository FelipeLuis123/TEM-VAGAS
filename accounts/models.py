from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
   matricula = models.CharField(max_length=10, unique=True)

   def __str__(self):
       return self.username
   
