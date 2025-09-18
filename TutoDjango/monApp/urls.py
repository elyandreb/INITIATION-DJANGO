from django.urls import path
from . import views

urlpatterns = [
    path("home/<param>",views.accueil ,name='accueil'),
    path("contact/", views.contact, name="contact"),
    path("info/", views.apropos, name="apropos"),
    path("produits/", views.listeproduits, name="listeproduits"),
    path("categories/", views.listecat, name="listecat"),
    path("statuts/", views.listestatut, name="listestatut"),
    path("rayons/", views.listerayons, name="listerayons"),
]