from django.db import models

from datetime import datetime



class player(models.Model):
    playerName = models.TextField()
    money = models.PositiveIntegerField()
    getOutOFJail = models.BooleanField(default=False)

class deed(models.Model):
    propertyName = models.TextField()
    cost = models.PositiveIntegerField()
    rent =  models.PositiveIntegerField()
    color =  models.CharField(max_length=10)
    houses = models.PositiveIntegerField()
    hotels = models.PositiveIntegerField()
    Owner =  models.OneToOneField(player,on_delete = models.CASCADE, related_name='owner') 
    currentPlayer =  models.ForeignKey(to=player, on_delete = models.CASCADE,related_name='current_player', default=None)
