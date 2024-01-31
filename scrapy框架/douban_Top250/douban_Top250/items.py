# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanTop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 电影名称
    evaluate = scrapy.Field()  # 电影评分
    No = scrapy.Field()  # 电影排名
    video = scrapy.Field() # 电影可播放平台