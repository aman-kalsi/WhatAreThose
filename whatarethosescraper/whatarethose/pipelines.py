# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WhatarethosePipeline(object):
    def process_item(self, item, spider):
        return item

class TotheDBPipline(object):
   
   def open_spider(self,spider):
       self.file = sqlite3.connect('Whatarethose.db')
       
       
   def proccess_item(self,item,spider):
       conn = sqlite3.connect('Whatarethose.db')
       c = conn.cursor() 
       c.execute("CREATE images IF NOT EXISTS(id REAL,image BLOB, url TEXT)")
       c.execute("INSERT INTO images VALUES('%s,%s')" % (item['files_urls'],item['files']))
       conn.commit()
       conn.close()
       