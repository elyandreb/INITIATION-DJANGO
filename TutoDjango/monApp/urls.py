from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path("home/<param>",views.accueil ,name='accueil'),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("info/", views.AboutView.as_view(), name="apropos"),
    path("produits/", views.listeproduits, name="listeproduits"),
    path("categories/", views.listecat, name="listecat"),
    path("statuts/", views.listestatut, name="listestatut"),
    path("rayons/", views.listerayons, name="listerayons"),
    path("home/", views.HomeView.as_view()),
    path("home/<param>", views.HomeView.as_view())
]