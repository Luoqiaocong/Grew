# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanTop250Pipeline:
    def open_spider(self, spider):
        print('开始获取数据')
        self.f = open('movie.json', 'w', encoding='utf-8')  # 打开文件
        self.f.write('[')

        # item就是yield后的movie_message对象

    def process_item(self, item, spider):
        # 转换成字典对象再写入文件
        item_dict = ItemAdapter(item).asdict()  # 转换成python字典对象
        self.f.write(json.dumps(item_dict, ensure_ascii=False) + ',')  # ensure_ascii=False解决中文问题

        return item  # 返回item对象给下一个管道

    def close_spider(self, spider):
        self.f.write(']')
        self.f.close()
        print('结束获取数据')