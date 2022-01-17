from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import games
from EBank.models import player
from .forms import playerForm, gameForm
from django.core.exceptions import ObjectDoesNotExist
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
    form = playerForm()
    currentGame = games.objects.get(gameName=game_name)
    context = {
        "form": form,
        'gameName':game_name,
        'message': '',
    }
    context['players_list'] = player.objects.filter(game__id=currentGame.id) 
    return render(request, 'players.html',context)





def deletePlayer(request, pk, gameName):
    form = playerForm()
    player_object = player.objects.get(id=pk)
    player_object.delete()
    return redirect(f"../../../{gameName}/players") #FIX THIS


def addPlayer(request,gameName):
    form = playerForm()
    playerName = request.POST['playerName']
    context = {
        "form": form,
        'gameName':gameName,
        'message': '',
    }
    currentGame = games.objects.get(gameName=gameName)
    try:
        new_player = player.objects.create(playerName = playerName, game = currentGame)
        new_player.save() 
    except ObjectDoesNotExist:
        print('not player')
    except IntegrityError:
        print('not player')        
    return redirect(f"../../../{gameName}/players") #FIX THIS