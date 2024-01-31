import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字，用于运行爬虫的时候使用的值
    name = "baidu"
    # 允许访问的域名  (如果不写，默认允许访问所有域名)
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址，指的是第一次要访问的域名,在 allowed_domains前面添加一个http://，后面添加一个/
    start_urls = ["http://www.baidu.com/"]

    # 是执行了start_urls之后执行的方法，方法中的response就是返回的那个对象，相当于response= requests.get()
    def parse(self, response):
        print('========================================')
        print(response.text)
