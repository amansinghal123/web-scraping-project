# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CelebrityItem(scrapy.Item):
    name = scrapy.Field()
    bio = scrapy.Field()
    img = scrapy.Field()
    urls = scrapy.Field()
    counter = scrapy.Field()