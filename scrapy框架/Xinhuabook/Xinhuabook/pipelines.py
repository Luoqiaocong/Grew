# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


import requests
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 必须在settings开启管道
class XinhuabookPipeline:
    def open_spider(self, spider):
        print('开始获取数据')
        self.f = open('book_message.json', 'w', encoding='utf-8')
        self.f.write('[')

    # item就是yield后的book_message对象
    def process_item(self, item, spider):
        # 转换成字典对象再写入文件
        item_dict = ItemAdapter(item).asdict()   # 转换成python字典对象
        self.f.write(json.dumps(item_dict, ensure_ascii=False) + ',')   # ensure_ascii=False解决中文问题

        return item    # 返回item对象给下一个管道

    def close_spider(self, spider):
        self.f.write(']')
        self.f.close()
        print('结束获取数据')


class XinhuabookDownloadPipline:

    def process_item(self, item, spider):
        url = 'http:' + item.get('picture')  # 下载图片

        with open(f'./books_picture/{item.get("name").replace("/", "or")}' + '.jpg', 'wb') as f:
            f.write(requests.get(url).content)

        # url = 'http:'+item.get('picture')
        # filename = './books_picture/'+item.get('name').replace("/", ",")+'.jpg'
        #
        # urllib.request.urlretrieve(url=url, filename=filename)

        return item   # 返回item对象给下一个管道
