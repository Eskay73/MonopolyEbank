from django.db import models

from Games.models import games



class player(models.Model):
    playerName = models.TextField()
    money = models.PositiveIntegerField(default=1500)
    getOutOFJail = models.PositiveIntegerField(default=0)
    game =  models.ForeignKey(to=games, on_delete = models.CASCADE, default="", editable=False, null=True)
    def __str__(self):
        return self.playerName

class deed(models.Model):
    propertyName = models.TextField()
    cost = models.PositiveIntegerField()
    rent =  models.PositiveIntegerField()
    color =  models.CharField(max_length=10)
    houses = models.PositiveIntegerField()
    hotels = models.PositiveIntegerField()
    Owner =  models.OneToOneField(player,on_delete = models.CASCADE, related_name='owner') 
    currentPlayer =  models.ForeignKey(to=player, on_delete = models.CASCADE,related_name='current_player', default=None)
    def __str__(self):
        return self.propertyName
