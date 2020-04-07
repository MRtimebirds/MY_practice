# -*- coding: utf-8 -*-
import scrapy
import json

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print(type(response.text))
        print(response.text)
        # useragent=dict(response.text)['user-agent']
        # useragent=json.loads(response.text)['user-agent']
        useragent=eval(response.text)['user-agent']
        print('*'*30)
        print(useragent)
        print('*'*30)
        yield scrapy.Request(self.start_urls[0],dont_filter=True) #dont_filter=True是不使用过滤