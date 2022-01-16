from django.db import models
from datetime import  datetime


# Create your models here.
class games(models.Model):
    id = models.IntegerField(primary_key=True)
    gameName = models.CharField(max_length=50,unique = True)
    result = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.gameName