from django.db import models
from datetime import  datetime

from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT

# Create your models here.
class games(models.Model):
    gameName = models.CharField(max_length=50)
    result = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.now())
    