from django.db import models

# Create your models here.


class Advertise(models.Model):
    datetime = models.CharField(max_length=300)
    cislo_inzeratu = models.CharField(max_length=300)
    dispozicia = models.CharField(max_length=300)
    plocha = models.CharField(max_length=300)
    cena = models.CharField(max_length=300)
    poplatky = models.CharField(max_length=300)
    vratna_kaucia = models.CharField(max_length=300)
    mesto = models.CharField(max_length=300)
    mestska_cast = models.CharField(max_length=300)
    typ_vlastnictva = models.CharField(max_length=300)
    typ_budovy = models.CharField(max_length=300)
    penb = models.CharField(max_length=300)
    poschodie = models.CharField(max_length=300)
    balkon = models.CharField(max_length=300)
    terasa = models.CharField(max_length=300)
    sklep = models.CharField(max_length=300)
    lodzia = models.CharField(max_length=300)
    parkovanie = models.CharField(max_length=300)
    vytah = models.CharField(max_length=300)
    garaz = models.CharField(max_length=300)
