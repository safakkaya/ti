from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class ItemDataItem(PortiaItem):
    Image = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Cat_1 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Brand = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Price = scrapy.Field(
        input_processor=Price(),
        output_processor=Join(),
    )
    Cat_2 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Size = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Colour = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Cat_3 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Name = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class SaleDataItem(PortiaItem):
    Cat_3 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Size = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    PriceSale = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    PriceRrp = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Cat_1 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Image = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Name = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Cat_2 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Colour = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
