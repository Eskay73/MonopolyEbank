from django.contrib import admin
from django.urls import  path

from . import views

urlpatterns = [
    # urls used in Games app for reference
    # path('',views.index,name='index'),
    # path('addGame',views.addGame,name='addGame'),
    # path('<str:game_name>/players',views.players,name='players'),
    # path("delete/<int:pk>/<str:gameName>/", views.deletePlayer, name="deletePlayer"),
    # path("add/<str:gameName>/", views.addPlayer, name="addPlayer"),
    # path('games',views.gamesList,name='gamesList'), 
]
