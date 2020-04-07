# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# #保存在json文件中
# from scrapy.exporters import JsonLinesItemExporter
# class JxsqPipeline(object):
#     def __init__(self):
#         #创建文件
#         self.fp=open('jxsq.json','wb')
#         self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#     #当停止爬虫时关闭文件
#     def __del__(self):
#         self.fp.close()
#         self.exporter.finish_exporting()
#     def start_spider(self,spider):
#         print('爬虫开始了，冲冲冲**************************************')
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#     def close_spider(self,spider):
#         print('爬虫结束了,撒花撒花花撒花花花********************************************')
#
# import json
# class JxsqPipeline(object):
#     def __init__(self):
#         #创建文件
#         self.fp=open('jxsq.json','w',encoding='utf-8')
#     #当停止爬虫时关闭文件
#     def __del__(self):
#         self.fp.close()
#     def start_spider(self,spider):
#         print('爬虫开始了，冲冲冲**************************************')
#     def process_item(self, item, spider):
#         item=json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item)
#         return item
#     def close_spider(self,spider):
#         print('爬虫结束了,撒花撒花花撒花花花********************************************')


#保存在mongoDB数据库里
# import pymongo
# class JxsqPipeline(object):
#     def __init__(self):
#         #创建mongo连接
#         self.client=pymongo.MongoClient()
#         #创建数据库，名为jxsq
#         self.db=self.client.jxsq
#         #创建集合，名为jxsq
#         self.collection=self.db.jxsq
#     #当停止爬虫时关闭文件
#     def __del__(self):
#         self.client.close()
#     def start_spider(self,spider):
#         print('爬虫开始了，冲冲冲**************************************')
#     def process_item(self, item, spider):
#         item=dict(item)
#         self.collection.insert(item)
#         return item
#     def close_spider(self,spider):
#         print('爬虫结束了,撒花撒花花撒花花花********************************************')


#保存在mysql数据库中
import pymysql
class JxsqPipeline(object):
    def __init__(self):
        #创建mysql连接
        self.conn=pymysql.Connect(host='localhost',port=3306,user='root',password='123',db='jxsq',charset='utf8mb4')
        #建立cursor指针
        self.cursor=self.conn.cursor()
    #当停止爬虫时关闭数据库
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    def start_spider(self,spider):
        print('爬虫开始了，冲冲冲**************************************')
    def process_item(self, item, spider):
        item=dict(item)
        sql="""insert into jxsq(classification,title,times,publisher,viewnum,article)
          values(%s,%s,%s,%s,%s,%s)"""
        l=(item['classification'],item['title'],item['times'],item['publisher'],item['viewnum'],item['article'])
        self.cursor.execute(sql,l)
        self.conn.commit()
        return item
    def close_spider(self,spider):
        print('爬虫结束了,撒花撒花花撒花花花********************************************')

#使用异步下载
# import pymysql
# from pymysql import cursors
# from  twisted.enterprise import adbapi
# class JxsqPipeline(object):
#     def __init__(self):
#         #创建mysql连接
#         self.adbpool=adbapi.ConnectionPool('pymysql',host='localhost',port=3306,user='root',password='123',db='jxsq',charset='utf8mb4',cursorclass=cursors.DictCursor)
#     #当停止爬虫时关闭数据库
#     def __del__(self):
#         self.adbpool.close()
#     def start_spider(self,spider):
#         print('爬虫开始了，冲冲冲**************************************')
#     def process_item(self, item, spider):
#         self.adbpool.runInteraction(self.insert_item,item)
#         return item
#     def insert_item(self,cursor,item):
#         item=dict(item)
#         sql="""insert into jxsq(classification,title,times,publisher,viewnum,article)
#           values(%s,%s,%s,%s,%s,%s)"""
#         l=(item['classification'],item['title'],item['times'],item['publisher'],item['viewnum'],item['article'])
#         cursor.execute(sql,l)
#
#     def close_spider(self,spider):
#         print('爬虫结束了,撒花撒花花撒花花花********************************************')