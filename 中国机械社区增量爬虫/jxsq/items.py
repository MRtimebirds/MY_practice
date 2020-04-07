# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JxsqItem(scrapy.Item):
    classification=scrapy.Field()
    title=scrapy.Field()
    publisher=scrapy.Field()
    times=scrapy.Field()
    viewnum=scrapy.Field()
    article=scrapy.Field()