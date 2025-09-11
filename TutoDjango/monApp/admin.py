from django.contrib import admin
from .models import Contenir, Produit, Categorie, Statut, Rayon


class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "date_fabrication", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "date_fabrication"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ('intituleProd', 'date_fabrication')
    list_filter = ('statut', 'date_fabrication')

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

