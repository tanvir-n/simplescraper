# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class BookItem(Item):
    title = Field()
    price = Field()
    image_url = Field()
    url = Field()
    description = Field()
    upc = Field()
    product_type = Field()
    tax = Field()
    available = Field()