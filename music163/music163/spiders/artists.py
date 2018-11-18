# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


# 抓取入驻歌手
class ArtistsSpider(scrapy.Spider):
    name = 'artists'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def start_requests(self):
        url = 'https://music.163.com/weapi/artist/list?csrf_token='
        yield Request(url, method='post', callback=self.parse)

    def parse(self, response):
        self.logger.debug(response.text)
        pass
