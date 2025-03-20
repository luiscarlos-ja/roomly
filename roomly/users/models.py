from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # Campos adicionales
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    
    # Puedes agregar más campos según necesites