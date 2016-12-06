from django.db import models

# Create your models here.

class Institution(models.Model):
    nom = models.CharField(max_length=100, null=True)
    source = models.TextField(null=True)
    article = models.TextField(null=True)
    type = models.CharField(max_length=100, null=True)
    pays = models.CharField(max_length=100, null=True)
    where = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom

class Technology(models.Model):
    nom = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    prix = models.FloatField(null=True)
    mobility = models.CharField(max_length=100, null=True)
    languages = models.CharField(max_length=100, null=True)
    type_environnement = models.CharField(max_length=100, null=True)
    type_age = models.CharField(max_length=100, null=True)
    cat_assistance = models.CharField(max_length=100, null=True)
    cat_fonctions = models.CharField(max_length=100, null=True)
    cat_techno = models.CharField(max_length=100, null=True)
    tags = models.TextField(null=True)

    def __str__(self):
        return self.nom