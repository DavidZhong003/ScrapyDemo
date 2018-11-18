# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapy import Request, Spider
from scrapyseleniumtest.items import ProductItem
from scrapy.log import logger


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    # start_urls = ['http://www.taobao.com/']
    base_url = 'http://www.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                # meta 传值给下个函数
                yield Request(url, callback=self.parse, meta={'page': page}, dont_filter=True)
        pass

    def parse(self, response):
        logger.log(response.text)
        pass
