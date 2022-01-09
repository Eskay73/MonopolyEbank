from django.db import models

from Games.models import games



class player(models.Model):
    playerName = models.TextField()
    money = models.PositiveIntegerField()
    getOutOFJail = models.BooleanField(default=False)
    game =  models.ForeignKey(to=games, on_delete = models.CASCADE, default="", editable=False)

class deed(models.Model):
    propertyName = models.TextField()
    cost = models.PositiveIntegerField()
    rent =  models.PositiveIntegerField()
    color =  models.CharField(max_length=10)
    houses = models.PositiveIntegerField()
    hotels = models.PositiveIntegerField()
    Owner =  models.OneToOneField(player,on_delete = models.CASCADE, related_name='owner') 
    currentPlayer =  models.ForeignKey(to=player, on_delete = models.CASCADE,related_name='current_player', default=None)