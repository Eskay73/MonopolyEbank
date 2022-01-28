from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from .models import games
from EBank.models import player
# from .forms import playerForm, gameForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
# Create your views here.
