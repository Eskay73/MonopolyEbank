from django import forms
from django.forms import ModelForm
from EBank.models import player
from .models import games


class playerForm(forms.ModelForm):
    class Meta:
        model = player
        fields=('playerName',)
        labels = {
            'playerName': ('Player Name'),
        }
        widgets = {
            'playerName': forms.TextInput(attrs={'class': 'todo-form'},),
        }
        


class gameForm(forms.ModelForm):
    class Meta:
        model = games
        fields=('gameName',)
