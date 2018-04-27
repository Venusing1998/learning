# -*- coding: utf-8 -*-
import scrapy
#
from Itcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.itcst.cn']
    start_urls = ['http://www.itcst.cn/']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        # 用来存春所有的item字段的
        items = []
        for node in node_list:
            #创建item字段对象，用来存储信息
            item = ItcastItem()
            # .extract()将xpath对象转换为codUcodUUnicode

        # pass
