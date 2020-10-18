# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from map_site.models import Advertise


class WithoutrealestateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AdvertiseItem(DjangoItem):
    django_model = Advertise
