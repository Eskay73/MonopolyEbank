from django import forms
from django.forms import ModelForm
from EBank.models import player


class playerForm(forms.ModelForm):
    class Meta:
        model = player
        fields=('playerName',)