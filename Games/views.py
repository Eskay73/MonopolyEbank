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
        return HttpResponseRedirect('/') 


def players(request):
    form = playerForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        context['form'] = playerForm()
    context['players_list'] = player.objects.all()
    return render(request, 'players.html',context)

def editPlayer(request, pk):
    task = player.objects.get(id=pk)

    form = playerForm(instance=task)

    if request.method == "POST":
        form = playerForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("players")

    return render(request, "updateName.html", {"editName": form})

def deletePlayer(request, pk):
    player_object = player.objects.get(id=pk)
    player_object.delete()
    return redirect("index")
