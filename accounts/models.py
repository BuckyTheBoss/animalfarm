from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    street_address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Profile for user: {self.user.username}'