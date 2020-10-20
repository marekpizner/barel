import scrapy
import time
import re
import unicodedata
import time
from ..items import AdvertiseItem


class DataSpider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        for ids in range(0, 2):
            url = f'https://www.bezrealitky.sk/vypis/ponuka-prenajom/byt/bratislavsky-kraj?page={ids}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        base_selector = response.xpath(
            '//a[@class="product__link js-product-link"]')
        for sel in base_selector:
            link = sel.xpath('./@href').extract()
            link_text = sel.xpath('./text()').extract()
            url = "https://www.bezrealitky.sk" + \
                link[0]
            print(url)
            yield scrapy.Request(url, callback=self.parse_concrete_inzerat)

    def strip_accents(self, text):
        """
        Strip accents from input String.

        :param text: The input string.
        :type text: String.

        :returns: The processed String.
        :rtype: String.
        """
        try:
            text = unicode(text, 'utf-8')
        except (TypeError, NameError):  # unicode is a default on python 3
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)

    def text_to_id(self, text):
        """
        Convert input text to id.

        :param text: The input string.
        :type text: String.

        :returns: The processed String.
        :rtype: String.
        """
        text = self.strip_accents(text.lower())
        text = re.sub('[ ]+', '_', text)
        text = re.sub('[^0-9a-zA-Z_-]', '', text)
        return text

    def parse_concrete_inzerat(self, response):
        name = response.xpath("//h1//span/text()").get()
        name = self.text_to_id(name)
        table = response.xpath('//*[@class="table"]//tr')
        advertise = AdvertiseItem()
        advertise['datetime'] = int(time.time())
        advertise['name'] = name
        for row in table:
            row_name = row.xpath('th//text()').get()
            row_name = self.text_to_id(str(row_name))

            row_value = row.xpath('td//text()').get()

            if row_name in advertise.fields:
                advertise[row_name] = row_value
        # print(advertise.items())
        yield advertise
