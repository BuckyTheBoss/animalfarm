from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=200)
    legs = models.IntegerField()
    speed = models.IntegerField()
    color = models.CharField(max_length=200)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name