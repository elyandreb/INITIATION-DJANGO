from django import forms

from monApp.models import Categorie, Produit, Statut, Rayon

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        #fields = '__all__'
        exclude = ('categorie', 'statut')

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nomCat']

class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = ['libelle']

class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = ['nomRay']
