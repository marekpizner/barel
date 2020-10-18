from django.db import models

# Create your models here.


class Advertise(models.Model):
    datetime = models.CharField(max_length=30)
    cislo_inzeratu = models.CharField(max_length=30)
    dispozicia = models.CharField(max_length=30)
    plocha = models.CharField(max_length=30)
    cena = models.CharField(max_length=30)
    poplatky = models.CharField(max_length=30)
    vratna_kaucia = models.CharField(max_length=30)
    mesto = models.CharField(max_length=30)
    mestska_cast = models.CharField(max_length=30)
    typ_vlastnictva = models.CharField(max_length=30)
    typ_budovy = models.CharField(max_length=30)
    penb = models.CharField(max_length=30)
    poschodie = models.CharField(max_length=30)
    balkon = models.CharField(max_length=30)
    terasa = models.CharField(max_length=30)
    sklep = models.CharField(max_length=30)
    lodzia = models.CharField(max_length=30)
    parkovanie = models.CharField(max_length=30)
    vytah = models.CharField(max_length=30)
    garaz = models.CharField(max_length=30)
