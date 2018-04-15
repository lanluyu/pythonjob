# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

class PythonjobPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        scrapy_db = client['scrapy_db']       # 创建数据库 scrapy_db
        self.coll = scrapy_db['pythonjob']      # 创建数据库中的表格 jobs_ye

    def process_item(self, item, spider):
        self.coll.insert_one(item)
        return item
