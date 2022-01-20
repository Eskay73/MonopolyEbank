from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from Games.models import games

from .models import player

# Create your views here.
def Balance(request,gameName):
    context = {}
    currentGame = games.objects.get(gameName=gameName)
    context['gameName'] = gameName
    context['playersList'] = player.objects.filter(game__id=currentGame.id) 
    return render(request,'bank.html',context) 

def payMoney(request,gameName):
    payee_id = request.POST['payee']
    payer_id = request.POST['payer']
    amount = request.POST['amount']
    successT = True
    if amount:
        if payer_id!='Bank':
            payer = player.objects.get(id = payer_id)
            if payer.money > int(amount):
                payer.money= payer.money - int(amount)
                payer.save()
            else:
                successT = False
        if payee_id!='Bank' and successT:
            payee = player.objects.get(id = payee_id)
            payee.money= payee.money + int(amount)
            payee.save()
    return HttpResponseRedirect(f'../{gameName}')

    
