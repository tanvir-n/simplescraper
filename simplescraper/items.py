# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SimplescraperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(Item):
    title = Field()
    # price = Field()
    # upc = Field()
    # image_url = Field()
    # url = Field()
    # description = Field()
    # prod_type = Field()
    # tax = Field()
    # available = Field()