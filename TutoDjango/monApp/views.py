from django.shortcuts import render
from django.http import HttpResponse

from monApp.models import Categorie, Produit, Rayon, Statut
from django.views.generic import *

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


class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello Django " + self.kwargs.get('param', '')
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class ContactView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Contact us"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)