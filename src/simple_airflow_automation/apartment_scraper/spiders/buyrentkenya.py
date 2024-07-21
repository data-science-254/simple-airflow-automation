import scrapy


class BuyrentkenyaSpider(scrapy.Spider):
    name = "buyrentkenya"
    allowed_domains = ["www.buyrentkenya.com"]
    start_urls = ["https://www.buyrentkenya.com"]

    def parse(self, response):
        pass
