# -*- coding: utf-8 -*-
import scrapy


class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    allowed_domains = ['https://www.aliexpress.com/category/200216607/tablets.html']
    start_urls = ['http://https://www.aliexpress.com/category/200216607/tablets.html/']

    def parse(self, response):
        pass
