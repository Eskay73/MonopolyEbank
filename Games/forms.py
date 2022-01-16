from django import forms
from django.forms import ModelForm
from EBank.models import player
from .models import games



class playerForm(forms.ModelForm):
    class Meta:
        model = player
        fields=('playerName',)


class gameForm(forms.ModelForm):

    class Meta:
        model = games
        fields=('gameName',)
