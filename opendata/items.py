# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import Compose


def take_first(value):
    return value[0] if value else ""


def clean_string(value):
    return value.strip()


class MemberItem(scrapy.Item):
    name = scrapy.Field(output_processor=Compose(take_first,
                                                 clean_string))
    term = scrapy.Field(output_processor=Compose(take_first,
                                                 clean_string))
    province = scrapy.Field(output_processor=Compose(take_first,
                                                     clean_string))
    party = scrapy.Field(output_processor=Compose(take_first,
                                                  clean_string))
