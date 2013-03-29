# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
from scrapy.item import Item, Field

class IsBullshitItem(Item):
    title = Field()
    author = Field()
    tag = Field()
    date = Field()
    link = Field()