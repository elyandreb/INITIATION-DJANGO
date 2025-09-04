from django.shortcuts import render
from django.http import HttpResponse


def home(request, param=''):
    return HttpResponse("<h1>Bonjour "+param+" !</h1>")

def contact(request):
    return HttpResponse("<h1> Contactez nous</h1> <p> Ceci est un test </p>")

def apropos(request):
    return HttpResponse("<h1> About us</h1> <p> Ceci est un test </p>")