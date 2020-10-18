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


class Advertise(scrapy.Item):
    datetime = scrapy.item.Field()
    cislo_inzeratu = scrapy.item.Field()
    dispozicia = scrapy.item.Field()
    plocha = scrapy.item.Field()
    cena = scrapy.item.Field()
    poplatky = scrapy.item.Field()
    vratna_kaucia = scrapy.item.Field()
    mesto = scrapy.item.Field()
    mestska_cast = scrapy.item.Field()
    typ_vlastnictva = scrapy.item.Field()
    typ_budovy = scrapy.item.Field()
    penb = scrapy.item.Field()
    poschodie = scrapy.item.Field()
    balkon = scrapy.item.Field()
    terasa = scrapy.item.Field()
    sklep = scrapy.item.Field()
    lodzia = scrapy.item.Field()
    parkovanie = scrapy.item.Field()
    vytah = scrapy.item.Field()
    garaz = scrapy.item.Field()
