# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from logging import getLogger
from music163.items import ArtistItem
import re


# 抓取入驻歌手
def parse_artists(response):
    selector = response.selector
    artists = selector.xpath('//*[@id="m-artist-box"]/li[@class="sml"]')
    for artist in artists:
        artist_item = ArtistItem()
        artist_item['name'] = artist.xpath('./a[1]/text()').extract_first()
        artist_item['artist_url'] = artist.xpath('./a[1]/@href').extract_first()
        artist_item['artist_id'] = re.findall('[1-9]\d*', artist_item['artist_url'])[0]
        # //*[@id="m-artist-box"]/li[11]/a[2]
        artist_item['home_url'] = artist.xpath('./a[2]/@href').extract_first()
        if artist_item['home_url'] is not None:
            artist_item['home_id'] = re.findall('[1-9]\d*', artist_item['home_url']).pop()
        else:
            artist_item['home_id'] = None
        ArtistsSpider.logger.info(artist)
        ArtistsSpider.logger.info(artist_item)


class ArtistsSpider(scrapy.Spider):
    name = 'artists'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']
    logger = getLogger("artists_spider")

    def start_requests(self):
        # 推荐歌手链接
        # url = 'https://music.163.com/#/discover/artist'
        url = 'https://music.163.com/#/discover/artist/cat?id=1001&initial=65'
        yield Request(url, method='post', callback=self.parse)

    def parse(self, response):
        parse_artists(response)
        pass
