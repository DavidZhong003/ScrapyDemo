# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import log
from taotao.items import SwisseItem
import re


class ArtistsSpider(scrapy.Spider):
    name = 'swisse'
    allowed_domains = ['https://www.chemistwarehouse.com.au']
    host = "https://www.chemistwarehouse.com.au"

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            yield Request(url=self.host + "/shop-online/" + keyword, callback=self.parse,
                          dont_filter=True)
    pass

    def parse(self, response):
        print("==========================开始执行=======================")
        print("url:"+response.url)
        # 爬去本页
        yield from self.parse_one_page(response)
        # 判断是否有下一页 //*[@id="Left-Content"]/div[10]/div[2]/a[6]
        next_page = \
            response.selector.xpath('//*[@id="Left-Content"]/div[10]/div[2]/a[6]/@href').extract()[
                0]
        if next_page not in response.url:
            yield Request(url="https://www.chemistwarehouse.com.au" + next_page, callback=self.parse,
                          dont_filter=True)
        print("==========================结束=======================")

    def parse_one_page(self, response):
        sel = response.selector
        # tbody
        goods = sel.xpath('//*[@id="p_lt_ctl06_pageplaceholder_p_lt_ctl00_wPListC_lstElem"]')
        for good in goods.xpath('./tr/td'):
            try:
                item = SwisseItem()
                item['name'] = good.xpath('.//a/@title').extract()[0]
                # .//a/div/div[1]/div[2]/img[1]
                item['image'] = good.xpath('.//a/div/div[1]/div[2]/img[1]/@src').extract()[0]
                # .//a/div/div[2]/span[1]
                item['prices'] = good.xpath('.//a/div/div[2]/span[1]/text()').extract()[0].strip()
                yield item
            except Exception:
                pass
