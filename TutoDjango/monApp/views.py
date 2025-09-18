from django.shortcuts import render
from django.http import HttpResponse

from monApp.models import Categorie, Produit, Statut


def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def contact(request):
    return HttpResponse("<h1> Contactez nous</h1> <p> Ceci est un test </p>")

def apropos(request):
    return HttpResponse("<h1> About us</h1> <p> Ceci est un test </p>")

def listeproduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def listecat(request):
    cats = Categorie.objects.all()
    ul = "<ul>"
    for c in cats:
        ul += "<li>" + c.nomCat + "</li>"
    ul += "</ul>"
    return HttpResponse("<h1> Liste des catégories </h1>" + ul)

def listestatut(request):
    stats = Statut.objects.all()
    ul = "<ul>"
    for s in stats:
        ul += "<li>" + s.libelle + "</li>"
    ul += "</ul>"
    return HttpResponse("<h1> Liste des statuts </h1>" + ul)
