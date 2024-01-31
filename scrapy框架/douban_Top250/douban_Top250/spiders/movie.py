import scrapy

from douban_Top250.items import DoubanTop250Item


class MovieSpider(scrapy.Spider):
    name = "movie"  # 爬虫名称
    allowed_domains = ["movie.douban.com"]  # 允许爬取的域名
    page_url = "https://movie.douban.com/top250?start={}&filter="  # 爬取的网页

    def start_requests(self):
        for page in range(0, 226, 25):  # 从0开始，每次增加25，到226结束。
            url = self.page_url.format(page)  # 格式化url
            yield scrapy.Request(  # 返回一个Request对象
                url=url,
                callback=self.parse
            )

    # 解析页面，获取电影名称，评分，视频可播放平台，并保存到数据库中。
    def parse(self, response):
        # start = 0
        li_list = response.xpath('//div[@class="info"]')  # 获取包含电影信息的div标签。
        for i in li_list:
            # extract_first获取第一个符合的元素
            name = i.xpath('.//a/span[1]/text()').extract_first()  # 获取电影名称。
            evaluate = int(i.xpath('.//div[@class="star"]//span[2]/text()').extract_first())  # 获取电影评分。
            movie_url = i.xpath('.//div[@class="hd"]//a/@href').extract_first()  # 获取电影详情页的url。

            yield scrapy.Request(url=movie_url, callback=self.parse_video, meta={'name': name, 'evaluate': evaluate})  # 返回一个Request对象

    def parse_video(self, response):
        name, evaluate = response.meta['name'], response.meta['evaluate']  # 获取电影名称和评分。

        playable = response.xpath('//div[@class="gray_ad"]//li//a/@data-cn')  # 获取'可播放'这个元素  # 有些电影没有可播放平台，所以要判断一下。

        video = playable.extract() if playable else '暂无'  # 如果为空，则返回'暂无'，否则返回列表(extract转化为列表)。
        No = int(response.xpath('//span[@class="top250-no"]/text()').extract_first()[3:])  # 只保留电影排名数字，并转化为整型
        # No = response.xpath('//span[@class="top250-no"]/text()').extract_first()

        movie_message = DoubanTop250Item(name=name, evaluate=evaluate, No=No, video=video)  # 实例化一个DoubanTop250Item对象
        yield movie_message     # 返回一个DoubanTop250Item对象


