from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    street_address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Profile for user: {self.user.username}'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('hello world')
    if created:
        Profile.objects.create(user=instance)

