# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Images360Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


class ImagesItem(Item):
    collection = table = 'images'
    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
    tag = Field()
    pass
