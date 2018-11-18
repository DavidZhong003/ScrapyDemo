# -*- coding: utf-8 -*-
import scrapy

from tutorial.items_quotes import QuoteItem


class QuotesSpider(scrapy.Spider):
    # name 区分不同spider
    name = 'quotes'
    # allowed_domains 允许爬去域名
    allowed_domains = ['quotes.toscrape.com']
    # 初始url列表
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # css 筛选器
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        # 下一页
        next_pager = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next_pager)
        yield scrapy.Request(url, callback=self.parse)
        pass
