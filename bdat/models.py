from django.db import models

# Create your models here.

class Institution(models.Model):
    nom = models.CharField(max_length=100)
    source = models.TextField(null=True)
    article = models.TextField(null=True)
    type = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    where = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Technology(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True)
    prix = models.FloatField(null=True)
    mobility = models.CharField(max_length=100)
    languages = models.TextField(null=True)
    type_cif = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    type_environnement = models.CharField(max_length=100)
    type_age = models.CharField(max_length=100)
    image = models.ImageField(upload_to='/img', null=True)
    cat_assistance = models.CharField(max_length=100)
    cat_fonctions = models.CharField(max_length=100)
    cat_techno = models.CharField(max_length=100)
    tags = models.TextField(null=True)

    def __str__(self):
        return self.nom