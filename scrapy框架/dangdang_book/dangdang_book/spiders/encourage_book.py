import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EncourageBookSpider(CrawlSpider):
    name = "encourage_book"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/pg1-cp01.41.50.00.00.00.html"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        li_list = response.xpath('')
