from django.contrib import admin
from .models import Contenir, Produit, Categorie, Statut, Rayon


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('intituleProd', 'prixUnitaireProd')

admin.site.register(Produit, ProduitAdmin)

class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1  # nombre de lignes vides par défaut
    
class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Statut)
admin.site.register(Rayon)

