from django.contrib import admin
from django.contrib import admin
from .models import Produit, Categorie, Statut, Rayon

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Statut)
admin.site.register(Rayon)

