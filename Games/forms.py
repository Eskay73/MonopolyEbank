from django import forms
from django.forms import ModelForm
from EBank.models import player
from .models import games
from django.forms.widgets import TextInput,Textarea



class playerForm(forms.ModelForm):
    class Meta:
        model = player
        fields=('playerName',)


class gameForm(forms.ModelForm):

    class Meta:
        model = games
        fields=('gameName',)
        widgets={
            'gameName':TextInput(attrs={'class': 'form-control',
                                        'placeholder':'Game name',
                                        'onkeyup': 'success()',
                                        'id':'gameName',
                                        'name':'gameName', 
                                        }),

            }
    def __init__(self, *args, **kwargs): 
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['gameName'].label = ''