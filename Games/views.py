from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import games
from EBank.models import player
from .forms import playerForm, gameForm
from django.db import IntegrityError



def index(request):
    if(games.objects.first()):
        hasGame =True
    else:
        hasGame =False
    form = gameForm()
    context = {
        'hasGame':hasGame,
        'form':form
    }
    return render(request, 'index.html',context)


def addGame(request):
        if request.method=='POST':
            game_name = request.POST['gameName']
            bool = games.objects.filter(gameName=game_name).first()
            if games.objects.filter(gameName=game_name).first():
                return HttpResponseRedirect(f'/{game_name}/players') 
            game = games(gameName=game_name)
            game.save()
        return HttpResponseRedirect(f'/{game_name}/players') 


def players(request,game_name):
    currentGame = games.objects.get(gameName=game_name)
    form = playerForm(request.POST or None)
    context = {
        "form": form,
        'gameName':game_name,
        'message': '',
    }
    context['players_list'] = player.objects.filter(game__id=currentGame.id) 
    try:
        if form.is_valid():
            currentPlayer = form.save()
            currentPlayer.game=currentGame
            currentPlayer.save()
    except IntegrityError:
        context['message'] = 'player already exists'   
        context['form'] = playerForm()
    return render(request, 'players.html',context)





def deletePlayer(request, pk, gameName):
    player_object = player.objects.get(id=pk)
    player_object.delete()
    return redirect(f"../../../{gameName}/players") #FIX THIS
