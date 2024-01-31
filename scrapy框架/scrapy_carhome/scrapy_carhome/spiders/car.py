import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-36-152.html"]

    def parse(self, response):
        print('====================')
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span//span/text()')

        for i in range(len(name_list)):
            print(name_list[i].extract(), price_list[i].extract())   # extract()方法可以将xpath对象转换为字符串

