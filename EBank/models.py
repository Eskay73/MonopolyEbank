from django.db import models

# Create your models here.
class player(models.Model):
    pass

class property(models.Model):
    propertyName = models.TextField()
    cost = models.IntegerField()
    rent =  models.IntegerField()
    color =  models.TextField()
    buildings : models.IntegerField()
    Owner : models.TextField()
