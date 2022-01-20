from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
        path('<str:gameName>',views.Balance,name='Balance'),
        path('<str:gameName>/pay',views.payMoney,name='payMoney'), 
]
