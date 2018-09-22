# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class SpidebilibiliPipeline(object):
    def __init__(self):
        # host = settings['MONGODB_HOST']
        # port = settings['MONGODB_PORT']
        # dbName = settings['MONGODB_DBNAME']
        # client = pymongo.MongoClient(host=host,port=port)
        # tdb = client[dbName]
        # self.post = tdb[settings['MONGODB_DOCNAME']]

        self.connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = self.connection[settings['MONGODB_DBNAME']]
        self.collection = db[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        video_infor = dict(item)
        self.collection.insert(video_infor)
        return item
