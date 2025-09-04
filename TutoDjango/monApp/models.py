from django.db import models

class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    # Relation CIF : chaque produit appartient à 1 catégorie (0,N côté catégorie 1,1 côté produit)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="produits",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.intituleProd

class Rayon(models.Model):
    idRay = models.AutoField(primary_key=True)
    nomRay = models.CharField(max_length=100)

    def __str__(self):
        return self.nomRay

class Contenir(models.Model):
    idCont = models.AutoField(primary_key=True)
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name="rayons"
    )
    rayon = models.ForeignKey(
        Rayon,
        on_delete=models.CASCADE,
        related_name="produits"
    )

    def __str__(self):
        return f"{self.produit.intituleProd} dans {self.rayon.nomRay}"
