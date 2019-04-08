# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TaotaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


class SwisseItem(scrapy.Item):
    name = Field()
    image = Field()
    prices = Field()
    pass
