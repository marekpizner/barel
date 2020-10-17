import scrapy
import time
import re
import unicodedata


class DataSpider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        for ids in range(0, 5):
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
        name = response.xpath("//h1//span/text()").getall()
        price = response.xpath(
            '//p[@class="heading__side text-right"]/text()').get()

        table = response.xpath('//*[@class="table"]//tr')

        for row in table:
            # print(row)
            row_name = row.xpath('th//text()').get()
            row_name = self.text_to_id(str(row_name))

            row_value = row.xpath('td//text()').get()
            print(row_name, row_value)

        # dname = table[3].xpath('th//text()')[0].get().strip()
        # dispozition = table[3].xpath('td//text()')[0].get().strip()
        # area = table[4].xpath('td//text()')[0].get().strip()
        # price_2 = table[5].xpath('td//text()')[0].get().strip()
        # fees = table[6].xpath('td//text()')[0].get().strip()
        # caution = table[7].xpath('td//text()')[0].get().strip()
        # city = table[8].xpath('td//text()')[0].get().strip()
        # ownership = table[9].xpath('td//text()')[0].get().strip()
        # building = table[10].xpath('td//text()')[0].get().strip()
        # floor = table[13].xpath('td//text()')[0].get().strip()
        # balcony = table[14].xpath('td//text()')[0].get().strip()

        # print('Name: ', name[1].strip(), price.strip())
        # print('3', dname,  dispozition)
        # print('4', area)
        # print('5', price_2)
        # print('6', fees)
        # print('7', caution)
        # print('8', city)
        # print('9', ownership)
        # print('10', building)
        # print('13', floor)
        # print('14', balcony)
