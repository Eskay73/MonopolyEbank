from django.db import models
import datetime
class Player(models.Model):
    playerName = models.CharField(max_length=50)
    money = models.PositiveIntegerField()
    getOutOFJail = models.BooleanField()
    properties  = models.ForeignKey(to=Property, on_delete = models.CASCADE)
    game  = models.ForeignKey(to=Game, on_delete = models.CASCADE)


class Game(models.Model):
    Gamename = models.CharField(max_length=50)
    Result = models.CharField(max_length=10)
    createdAt = models.DateTimeField(default=datetime.now, blank=True)