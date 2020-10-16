import scrapy


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
            print(link, link_text)
            url = "https://www.bezrealitky.sk" + \
                link[0]
            print('Url: ', url)
            return scrapy.Request(url, callback=self.parse_concrete_inzerat)

    def parse_concrete_inzerat(self, response):
        name = response.xpath(
            '//span/text()').get()

        print('Name: ', name)
