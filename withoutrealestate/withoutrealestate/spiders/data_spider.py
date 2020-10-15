import scrapy


class DataSpider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        for ids in range(0, 13):
            url = f'https://www.bezrealitky.sk/vypis/ponuka-prenajom/byt/bratislavsky-kraj?page={ids}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        base_selector = response.xpath(
            '//a[@class="product__link js-product-link"]')
        for sel in base_selector:
            link = sel.xpath('./@href').extract()
            link_text = sel.xpath('./text()').extract()
            print(link, link_text)
