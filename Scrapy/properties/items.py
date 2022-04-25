# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import pandas as pd

class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    ward = scrapy.Field()
    dist = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    area = scrapy.Field()
    compass = scrapy.Field()

    # # Housekeeping fields
    # url = scrapy.Field()
    # project = scrapy.Field()
    # spider = scrapy.Field()
    # server = scrapy.Field()
    # date = scrapy.Field()