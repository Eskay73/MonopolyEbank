from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addGame',views.addGame,name='addGame'),
    path('players',views.players,name='players'),
    path("edit/<int:pk>/", views.editPlayer, name="editName"),
    path("delete/<int:pk>/", views.deletePlayer, name="deletePlayer"), 
]
