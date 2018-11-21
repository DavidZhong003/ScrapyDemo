# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Music163Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    artist_url = Field()
    home_url = Field()
    pass


class ArtistItem(scrapy.Item):
    name = Field()
    artist_url = Field()
    artist_id = Field()
    home_id = Field()
    home_url = Field()
    pass
