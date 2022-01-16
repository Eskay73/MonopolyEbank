from typing import ContextManager
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import games
from EBank.models import player
from .forms import playerForm


def index(request):
    if(games.objects.first()):
        hasGame =True
    else:
        hasGame =False

    context = {
        'hasGame':hasGame
    }
    return render(request, 'index.html',context)


def addGame(request):
        if request.method=='POST':
            game_name = request.POST['gameName']
            game = games(gameName=game_name)
            game.save()
        return HttpResponseRedirect(f'/{game_name}/players') 


def players(request,game_name):
    form = playerForm(request.POST or None)
    context = {
        "form": form,
        'gameName':game_name
    }
    currentGame = games.objects.get(gameName=game_name)
    if form.is_valid():
        currentPlayer = form.save()
        currentPlayer.game=currentGame
        currentPlayer.save()
        context['form'] = playerForm()
    context['players_list'] = player.objects.filter(game__id=currentGame.id)
    return render(request, 'players.html',context)



def deletePlayer(request, pk, gameName):
    player_object = player.objects.get(id=pk)
    player_object.delete()
    return redirect(f"../../../{gameName}/players")
