from django.shortcuts import render
from django.http import HttpResponse

from monApp.models import Categorie, Produit, Rayon, Statut


def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def contact(request):
    return render(request, 'monApp/contact.html')

def apropos(request):
    return render(request, 'monApp/about.html')

def listeproduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def listecat(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categorie.html',{'cats': cats})

def listestatut(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'stats': stats})

def listerayons(request):
    rays = Rayon.objects.all()
    return render(request, 'monApp/list_rayon.html',{'rays': rays})
