from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=25, primary_key=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False)
    # telefono = models.CharField(max_length=10, null=False, blank=False)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "email"]
    
    class Meta:
        db_table = "usuarios"
