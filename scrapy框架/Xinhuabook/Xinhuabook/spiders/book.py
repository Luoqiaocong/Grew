import scrapy
import os
from Xinhuabook.items import XinhuabookItem

os.makedirs('./books_picture', exist_ok=True)


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["search.xhsd.com"]  # 主要请求的网址
    base_url = 'https://search.xhsd.com/search?frontCategoryId=42&pageNo=1'
    start_urls = [base_url]


    def parse(self, response):
        li_list = response.xpath('//ul[@class="shop-search-items-img-type"]//li')
        for li in li_list:
            # 每个li都是selector对象，再次使用xpath就可以获取到对应的信息了
            picture = li.xpath('.//img/@data-original').extract_first()
            name = li.xpath('.//p/a/text()').extract_first()
            author = li.xpath('.//p[2]/span/text()').extract_first()
            price = li.xpath('.//p[3]//span/text()').extract_first()
            print(picture, name, author, price)

            book_message = XinhuabookItem(picture=picture, name=name, author=author, price=price)

            yield book_message  # 获取一个book_message就将它交给piplines

        for i in range(5):
            url = self.base_url.replace('pageNo=1', 'pageNo='+str(i+2))
            # Scrapy.Requests就是调用scrapy的get请求
            # url就是请求的地址，callback就是你要请求的函数（不需要加圆括号）
            yield scrapy.Request(url=url, callback=self.parse)
