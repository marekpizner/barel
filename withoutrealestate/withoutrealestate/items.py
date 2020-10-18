# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import attr


class WithoutrealestateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


@attr.s
class Advertise(scrapy.Item):
    datetime = = attr.ib()
    cislo_inzeratu = attr.ib()
    dispozicia = attr.ib()
    plocha = attr.ib()
    cena = attr.ib()
    poplatky = attr.ib()
    vratna_kaucia = attr.ib()
    mesto = attr.ib()
    mestska_cast = attr.ib()
    typ_vlastnictva = attr.ib()
    typ_budovy = attr.ib()
    penb = attr.ib()
    poschodie = attr.ib()
    balkon = attr.ib()
    terasa = attr.ib()
    sklep = attr.ib()
    lodzia = attr.ib()
    parkovanie = attr.ib()
    vytah = attr.ib()
    garaz = attr.ib()
