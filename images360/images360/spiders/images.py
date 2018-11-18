# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import ImagesItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        # http://image.so.com/zj?ch=photography&sn=30&listtype=new&temp=1
        data = {'ch': 'photography', 'listtype': 'new'}
        base_url = "http://image.so.com/zj?"
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            # 第二个参数是callback
            yield Request(url, self.parse)
        pass

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImagesItem()
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            item['tag'] = image.get('tag')
            yield item
        pass
