from django import forms
from django.forms import ModelForm
from EBank.models import player
from .models import games
from django.forms.widgets import TextInput,Textarea


class playerForm(forms.ModelForm):
    class Meta:
        model = player
        fields=('playerName',)
        labels = {
            'playerName': ('Player Name'),
        }
        widgets = {
            'playerName': forms.TextInput(attrs={'class': 'todo-form shadow-sm bg-transparent border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', #appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
                                                'id':'playerName',
                                            },),
        }
        


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