# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class Dy1234Item(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class urlItem(scrapy.Item):
    ID = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()


class TorrentItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
